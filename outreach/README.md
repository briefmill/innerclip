# Inner Clip Season 4: partners and casting

Where the work stands as of Oct 14, 2026, and what happens next. Pulls together the Sept 13-14 prospecting session, the Oct 7-14 deck session, the Oct 8 call with Matt and Brandon, and the Oct 14 decisions.

## What already exists (built Sept 13-14)

- **Master plan (Google Doc):** "INNER CLIP 2027 Partnership & Casting Master Plan". https://docs.google.com/document/d/1n1quPo2BlTRRz8-egOIhKdH0pCjgekG1MiQS8ZYuvkA/edit. Its other eight docs are listed in the session report and are superseded by it.
- **Prospecting tool:** `D:\Github\Innerclip-prospecting\` on Lox's PC. Contains `prospect.py`, `fundability.py` and `INNERCLIP-PROSPECT-AUDIT.csv`, with all 999 companies scored.
  - 650 qualified, 496 with a contact route.
  - Top 40 ranked by ability to pay.
  - 28 pitches written.
  - 16 named decision makers.
  - 2 warm intros: Josiah Tully and Taylor Andrew.
- **Driver casting:** 73 FD drivers (34 PRO, 39 PROSPEC). Each has a verified Instagram handle and a personal DM line.
- **Nothing has been sent** (confirmed by Lox, Oct 14). The master doc's "Contacted" and "Emailed" labels are wrong. Every driver and brand is a first contact.

## Decks

| Deck | Link | State |
|---|---|---|
| Inner Clip x RACER | https://claude.ai/artifact/9wTGuo8MX1oGNwJK7r3CFx | v2 Oct 14. Needs 2 driver names and 3 budget numbers |
| Inner Clip for Drivers | https://claude.ai/artifact/3oaHuFo2RN9zaybhrgpoha | $50K / +$40K / $90K |
| Inner Clip for Brand Partners | https://claude.ai/artifact/FSFPDeWVSx7z7LTe2JCR9Z | 4 levels. Prices not set |
| Partner Deck (old) | https://claude.ai/artifact/4CpWVS4ew7KsQAWmAN6CG6 | On hold |

## Decisions (Oct 14)

1. **Drivers:** shortlist 4-8 for story and DM them now. Everyone else after the RACER outcome.
2. **Who pays:** drivers pay for their seat, mostly with sponsor money. Price never goes in a DM.
3. **Who sells partners:** Inner Clip and the drivers sell car brands. RACER's sales team sells non-car brands, if the deal happens.
4. **Season 3 brands:** Matt and Brandon lead the ask. Inner Clip supplies a one-page "here's exactly what you get" offer for each brand.
5. **DM channel:** Instagram DMs from Lox's personal account.
6. **Pipeline:** the Inner Clip tenant in Briefmill. Import `briefmill_import_drivers.csv` and `briefmill_import_brands.csv`.

## This week to SEMA

| When | What | Who |
|---|---|---|
| Now | Set partner prices for the 4 levels. Every brand call is blocked on this | Lox, Matt, Brandon |
| Now | Fill the RACER deck: 2 named drivers, 3 budget numbers. Agree non-negotiables | Lox, Matt, Brandon |
| Now | Pick the 4-8 driver shortlist. Follow, then DM, using the written personal lines | Lox |
| Now | Ask Josiah Tully for an intro to Discount Tire, and Taylor Andrew for O'Reilly. Hold their non-car intros (Monster, Milwaukee, Canon, GoPro) until after RACER | Lox |
| Now | Send the car-brand emails not on hold: Wisefab, Feal, Fuelab, Ignite, VP Racing, Vyper. **Strip the unsourced 434K claim first** | Lox |
| Next week | Scotto meeting (`racer_meeting_brief.md`) | Matt sets it |
| Oct 23-24, Long Beach | Ask the Season 3 incumbents: GT Radial, Borla, Liqui-Moly, Rugged Radios, K&N, Cool It, Logitech, Heat Wave. Meet shortlisted drivers | Matt, Brandon, Christian, Lox |
| After RACER | Non-car brands go to RACER's team, or back to Inner Clip if there's no deal | |
| Nov 3-6, SEMA | In-person meetings with car brands | |
| Nov 19 | RACER Creator Awards winners | |

## Held until the Season 3 incumbent in that category has been asked

| Category | Incumbent | Brands held |
|---|---|---|
| Tires | GT Radial | Kumho, Nitto, Kenda |
| Oil | Liqui-Moly | Pennzoil, Motul, Mobil 1 |
| Exhaust | Borla | AWE |
| Cooling | Cool It | Mishimoto |
| Sim hardware | Logitech | Simagic, MOZA |
| Batteries | Antigravity | Optima, XS Power |
| Clutch | Advanced Clutch | ACT, Clutchmasters |

## Open problems

- **Partner prices aren't set.** The Sept 13 rate card was Round $12.5K, Season $80K, Title $125K, aiming at $300K for 2027. It predates the new 4-level structure. Brandon suggested taking $5-10K from each of many partners. Pick one model.
- **Unsourced view numbers.** The 434K / 184K / 33.5K / 32.3K / 25.5K / 18.8K figures have no source. They're still in the 28 written pitches, the master doc, `EMAIL-SEQUENCES.md` and `BRAND.md`. Remove them before anything goes out.
- **The site rewrite isn't deployed.** The partner and driver page rewrites in the local `innerclip` site folder are uncommitted, next to unfinished Square shop changes.
- **The PC session (Inner Clip custom video assets) is still open.** It edits the same decks. Avoid editing a deck in both sessions at once.

## Files here

- `driver_dms.md`: DM scripts and follow-ups
- `briefmill_import_drivers.csv`: 73 drivers with handle, team, personal line, stage
- `briefmill_import_brands.csv`: 36 brands with tier, contact route, pitch line, lane (who sells), stage
- `racer_meeting_brief.md`: plan A/B/C, non-negotiables, questions for RACER (internal)
- `call_notes_pre_long_beach.md`: the Oct 8 call with Matt and Brandon
