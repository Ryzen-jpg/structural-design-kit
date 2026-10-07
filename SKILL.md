---
name: structural-design-kit
description: Use for any structural or civil design, check or design choice (buildings, steel or RC frames, foundations, slabs, walls, tanks, trusses, retaining structures). Applies the jurisdiction profile for the project's location; Nepal defaults to NBC + Indian Standards only.
---

# Structural design kit

A general workflow for structural design decisions of any type, size or material.
Code systems live in `jurisdictions/`. Project data never goes in this kit; it lives
with the project.

## 1. Pick the jurisdiction profile first

| Project location | Profile | Rule |
|---|---|---|
| Nepal | `jurisdictions/nepal.md` | NBC governs, Indian Standards fill gaps. No other codes unless the user asks for a labelled cross-check. |
| Anywhere else | Ask the user, then add a profile file using `jurisdictions/TEMPLATE.md` | Do not guess the governing code. |

Never mix partial factors, load combinations or material grades from different codes in one check.
A cross-check against another code is allowed only when the user asks, and it is labelled as outside the design basis.

## 2. Collect the required inputs

Work through `checklists/required-inputs.md`. If an input that changes the answer is missing,
ask for it before calculating. Do not assume soil type, seismic zone, importance class or occupancy.
Read the project's own notes or brief first, if the user has one.

## 3. Choose the system before sizing members

For any design choice (structural system, material, member type, foundation type), compare at least two
realistic options on:
- safety and reliability: load path continuity, redundancy, ductility, failure mode;
- cost and efficiency: material quantity, availability of sections and grades locally, construction speed;
- buildability: local skills, equipment, site access, inspection;
- durability and maintenance: exposure, corrosion, fire.

State the recommendation and the reason in two or three sentences. The engineer decides.

## 4. Design and check

Use the checklist for the element or system: `checklists/rc-frame.md`, `checklists/steel-frame.md`,
`checklists/foundations.md`, `checklists/seismic-mass.md`. Every check states the code, edition and clause.

A design is not finished at code pass/fail. Report utilisation ratios, the governing combination,
and where material can be saved without losing safety, ductility or buildability.

## 5. Software workflow

1. Freeze the architectural layout in AutoCAD.
2. Analyse and design in STAAD.Pro, set up per `checklists/staad-setup.md`.
3. Use Tekla only if detailing or quantities need it.

Hand-check the governing member of every element type independently (`calcs/` has scripts).
Software results that disagree with the hand check by more than about 10 to 15% need an explanation before use.

## 6. Report

Fill in `templates/design-basis.md`: codes and editions, inputs, load table, system choice and reason,
results with utilisation, drift, quantities, open items. Run `checklists/review.md` before handing over.

## Honesty rules

- A clause number, factor or limit not read from the code text in this session is marked "(verify)".
- Never invent a code value. If the value is not in `references/` and not provided, say so and ask for the code text.
- Unverified items are tracked in `VERIFY.md`.
- Only the code text itself counts as a source: the official publication, a scanned copy of it (e.g. archive.org BIS copies), or the user's own PDFs. Secondary explainer and aggregator sites never count, even when they look right. Excluded by name: iscodehub.com (checked 2026-10-07: wrong cover tolerance, invented exposure rules, wrong fire cover, no clause sources).
- Output is engineering support, not a stamped design. Final design needs review and sign-off by a licensed engineer in the project's jurisdiction.
