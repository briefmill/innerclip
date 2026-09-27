#!/usr/bin/env python3
"""Download YouTube captions for every video in a playlist and save them as
clean plain-text transcripts, ready to upload to a Claude project.

Usage:
    pip install yt-dlp
    python scripts/transcribe_playlist.py [PLAYLIST_URL] [OUTPUT_DIR]

Writes one Markdown file per video plus ALL_TRANSCRIPTS.md (everything
combined) into OUTPUT_DIR (default: transcripts/).
"""
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path

DEFAULT_PLAYLIST = "https://www.youtube.com/playlist?list=PLt5aoUkqmQM1c6OABoUVISrltJ8rGjZWi"


def list_videos(playlist_url):
    out = subprocess.run(
        ["yt-dlp", "--flat-playlist", "--dump-json", playlist_url],
        check=True, capture_output=True, text=True,
    ).stdout
    return [json.loads(line) for line in out.splitlines() if line.strip()]


def fetch_vtt(video_id, workdir):
    """Prefer creator-uploaded English captions, fall back to auto-generated."""
    subprocess.run(
        ["yt-dlp", "--skip-download", "--write-subs", "--write-auto-subs",
         "--sub-langs", "en.*,en", "--sub-format", "vtt",
         "-o", f"{workdir}/%(id)s.%(ext)s",
         f"https://www.youtube.com/watch?v={video_id}"],
        check=False, capture_output=True, text=True,
    )
    files = sorted(Path(workdir).glob(f"{video_id}*.vtt"))
    # Manual subs are named e.g. ID.en.vtt; auto subs ID.en-orig.vtt / ID.en.vtt.
    return files[0] if files else None


def vtt_to_text(vtt):
    """Strip timing/markup and the rolling-duplicate lines of auto captions."""
    lines, last = [], None
    for raw in vtt.splitlines():
        line = raw.strip()
        if (not line or line == "WEBVTT" or "-->" in line
                or re.match(r"^(Kind|Language|NOTE|STYLE)\b", line)
                or line.isdigit()):
            continue
        line = re.sub(r"<[^>]+>", "", line)  # inline word timings / styling
        line = re.sub(r"\s+", " ", line).strip()
        if line and line != last:
            lines.append(line)
            last = line
    # Rolling captions repeat the previous line as the first line of each cue.
    deduped = [l for i, l in enumerate(lines) if i == 0 or l != lines[i - 1]]
    text = " ".join(deduped)
    # Break into readable paragraphs of ~8 sentences-ish chunks.
    words = text.split()
    return "\n\n".join(" ".join(words[i:i + 150]) for i in range(0, len(words), 150))


def slug(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")[:80]


def main():
    playlist = sys.argv[1] if len(sys.argv) > 1 else DEFAULT_PLAYLIST
    outdir = Path(sys.argv[2] if len(sys.argv) > 2 else "transcripts")
    outdir.mkdir(parents=True, exist_ok=True)

    videos = list_videos(playlist)
    print(f"Found {len(videos)} videos")
    combined, missing = [], []

    with tempfile.TemporaryDirectory() as tmp:
        for n, v in enumerate(videos, 1):
            vid, title = v["id"], v.get("title") or v["id"]
            url = f"https://www.youtube.com/watch?v={vid}"
            vtt = fetch_vtt(vid, tmp)
            if not vtt:
                print(f"[{n}/{len(videos)}] NO CAPTIONS: {title}")
                missing.append(f"- {title} ({url})")
                continue
            body = vtt_to_text(vtt.read_text(encoding="utf-8"))
            doc = f"# {title}\n\nSource: {url}\n\n{body}\n"
            (outdir / f"{n:02d}-{slug(title)}.md").write_text(doc, encoding="utf-8")
            combined.append(doc)
            print(f"[{n}/{len(videos)}] ok: {title}")

    (outdir / "ALL_TRANSCRIPTS.md").write_text("\n\n---\n\n".join(combined), encoding="utf-8")
    if missing:
        (outdir / "MISSING_CAPTIONS.md").write_text(
            "# Videos without captions\n\n" + "\n".join(missing) + "\n", encoding="utf-8")
    print(f"Done: {len(combined)} transcripts, {len(missing)} without captions -> {outdir}/")


if __name__ == "__main__":
    main()
