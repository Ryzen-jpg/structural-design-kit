# Changelog

## 0.5.0 (2026-10-07)

Kathmandu site profile, checked against the user's NBC 105:2020 and NBC 108:1994 PDFs.

- New `jurisdictions/nepal-kathmandu.md`: overlay on the Nepal profile with Z = 0.35, soil type D, Table 4-1 parameters, design spectrum and Cd for I = 1.0, ground-condition rules (NBC 105 2.3.2/2.3.3, NBC 108 3.2/4.3), and open local-practice items
- SKILL.md routing table and `nepal.md` link to the overlay
- `references/nbc-105-2020.md`: noted that 4.1.4 cites Figure 4-4 but the zoning map is Figure 4-3, and the code's spelling in Table 4-4
- `VERIFY.md`: Kathmandu rows moved to Verified; open items are other Valley municipalities, reclassification, liquefaction method, permit editions, bylaws
- `calcs/test_nbc105_esm.py`: Kathmandu worked example (soil D, Z 0.35); 48 tests in total

## 0.4.0 (2026-10-07)

Filled from the user's Indian Standards PDF folder.

- IS 456 and IS 800 quick references fully verified from page images: IS 456 Tables 18-20, bond stress in compression, stirrup design; IS 800 Tables 4, 6, 10, 11, tension, compression, bending, LTB, combined forces, bolts and welds
- Corrected IS 800 Table 4 reading: DL+LL+CL+WL/EL has two cases (accompanying LL 1.05 with WL 0.6, and 0.53 with WL 1.2); DL+LL+AL is 1.0/0.35/0.35/1.0
- New `calcs/is800_compression.py` (Table 10 class, fcd, Pd), checked against printed Table 9(a); new `calcs/is456_shear.py` (Table 19/20, stirrup spacing); 47 tests in total
- New `references/is-library.md`: inventory of the local IS folder

## 0.3.0 (2026-10-07)

IS quick references checked against the full archive.org texts of IS 456:2000 and IS 800:2007.

- IS 456: partial factors, Table 18, stress block, xu,max/d, Annex G, beam/slab/column steel limits, stirrup spacing and minimum shear steel, span/depth, Table 16 cover with notes, development length and bond stress, slab k factor and axial shear factor verified. Added side-face, slab and spacing rows
- IS 800: Table 5, Table 7, Table 4, Table 6, low/high shear threshold and shear areas verified
- SKILL.md source rule: only the code text counts; secondary sites excluded, iscodehub.com by name
- Still open (OCR unreadable): IS 456 Tables 19/20 values, IS 800 Table 10 and several Section 8 to 10 coefficients

## 0.2.0 (2026-10-07)

Filled from the user's NBC library.

- `references/nbc-105-2020.md`: full parameter sheet verified against the code text (spectrum, soil, Z, I, period,
  seismic weight, Rmu/Omega, irregularity, drift, ESM, MRSM, parts and components, Annex A and B rules)
- Corrected Table 4-1 Ta values (0.1 / 0.5 s; text extraction had merged the footnote marker) and equation 10.3(1) (mu_p divides)
- `references/nbc-library.md`: inventory of the local NBC folder with editions
- Nepal profile: seismic detailing basis is NBC 105 Annex A/B; documented the NBC 110/111:1994 vs IS 456:2000/IS 800:2007 edition conflict and the default adopted
- Steel and RC checklists rewritten with Annex A/B requirements; STAAD and seismic-mass checklists gained NBC 105 items
- New `calcs/nbc105_esm.py` (spectrum, period, base shear, storey forces, drift) with 13 tests; 25 tests in total

## 0.1.0 (2026-10-07)

First version.

- General workflow skill (`SKILL.md`) for any structure type and material, with code systems in jurisdiction profiles
- Nepal profile: NBC governs, Indian Standards fill gaps, no other codes unless a labelled cross-check is requested
- Profile template for other countries
- Reference sheets: NBC 105:2020 (empty template, to be filled from code text), IS 456 and IS 800 quick references (all marked verify)
- Checklists: required inputs, seismic mass, RC frame, steel frame, foundations, STAAD setup, review
- Templates: design basis report, project brief
- Hand-check script: IS 456 singly reinforced rectangular flexure, with 12 tests
- Verification log
