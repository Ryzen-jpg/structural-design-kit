# Verification log

Everything under "Open" is from memory or secondary sources. Check against the code text, record the
clause and edition, then move the item to "Verified" in the same commit as the reference update.

## Open

### Nepal profile (`jurisdictions/nepal.md`)
- [ ] Confirm with the permit authority that IS 456:2000 and IS 800:2007 are accepted despite NBC 110/111:1994 wording (DUDBC RCC checklist uses IS 456:2000; no steel checklist seen yet)
- [ ] Which NBC 110 / NBC 111 Nepal amendments still apply when using the modern IS editions
- [ ] NBC 205:2024 scope limits (storeys, height, spans, occupancy); obtain the document
- [ ] NBC 101 and NBC 102 contents (not in library)
- [ ] NBC 103:1994 imposed load values by occupancy (document in library, not yet extracted)
- [ ] NBC 104:1994 wind procedure (document in library, not yet extracted)

### Kathmandu profile (`jurisdictions/nepal-kathmandu.md`)
- [ ] Z for Lalitpur, Bhaktapur, Madhyapur Thimi, Kageshori Manohara and Tokha: not in Table 4-5, read the zoning map (Figure 4-3)
- [ ] Soil class of any Valley municipality not in Table 4-4: 4.1.3.4 does not say
- [ ] Whether a Table 4-4 location can be reclassified: the text of 4.1.3.4 gives no route; ask the permit authority before relying on anything other than Type D
- [ ] Liquefaction screening method: neither NBC 105:2020 (2.3.3) nor NBC 108:1994 (3.2) gives one; take it from the geotechnical report and cite its source standard
- [ ] Which code editions the Kathmandu permit office enforces
- [ ] Current Kathmandu building bylaws (height, setbacks, coverage, FAR, fire access) and heritage-zone restrictions

### IS 456:2000 (`references/is-456-quickref.md`)
All quick-reference rows verified (archive.org text plus page images from the user's PDF).
- [ ] SP 16 printed Mu,lim coefficients vs exact formula values 0.1483 / 0.1380 / 0.1336 (SP 16 not in library; tests use +/-0.001)

### IS 800:2007 (`references/is-800-quickref.md`)
All quick-reference rows verified except Section 12 (not used in Nepal; NBC 105 Annex B governs).
- [ ] ISMB/ISHB section properties used in examples (IS 808 or manufacturer tables not in library)

### Other Indian Standards in the library (`references/is-library.md`)
- [ ] Extract IS 875 Parts 1, 2, 5; IS 1905; IS 4326; IS 10262; IS 2911-1-1 when a project needs them

### Software
- [ ] Whether the installed STAAD.Pro version has a built-in NBC 105:2020 seismic option

## Verified

| Item | Source | Checked by | Date |
|---|---|---|---|
| Kathmandu Z = 0.35 (Table 4-5); Table 4-4 lists Kathmandu, Lalitpur, Bhaktapur, Madhyapur Thimi, Kageshori Manohara, Tokha as Type D; 4.1.3.4 "sites located inside Kathmandu valley shall be obtained from Table 4-4"; Type D values in Table 4-1 (Ta 0.5, Tc 2.0, alpha 2.25, K 0.8, Ta = 0 for ESM); 7.5 V/VR scaling | NBC 105:2020 text extracted from the user's PDF | Claude | 2026-10-07 |
| 4.1.4 text cites Figure 4-4 for the zoning map; the map in the document is Figure 4-3 (misprint) | NBC 105:2020 text | Claude | 2026-10-07 |
| NBC 105:2020 2.3.2 and 2.3.3: seismic forces assume non-liquefying soil; soft liquefiable soil needs foundation design for soil movement, piles normally preferred, geotechnical advice | NBC 105:2020 text | Claude | 2026-10-07 |
| NBC 108:1994 3.2: ancient lake deposits (Kathmandu Valley named) investigated for liquefaction; 4.3: 20 m exploration depth should suffice for liquefaction analysis | NBC 108:1994 text extracted from the user's PDF | Claude | 2026-10-07 |
| NBC 105:2020 parameters: analysis methods, Table 3-1, combinations 3.6, spectrum 4.1 and Table 4-1, soil types, Z Table 4-5, I Table 4-6, SLS and vertical spectra, period 5.1, seismic weight Table 5-1, Table 5-2, irregularity 5.5, drift 5.6, eccentricity 5.7, ESM 6, MRSM 7, parts 10 | NBC 105:2020 code text (user's copy) | Claude | 2026-10-07 |
| Table 4-1 Ta = 0.1 s (A, B, C) and 0.5 s (D), Ta = 0 for ESM; equation 4.1(2) third branch has both (Tc/T) terms squared | Rendered page 20 of NBC 105:2020 | Claude | 2026-10-07 |
| Equation 10.3(1): Fp = Z (1 + hp/H)(ap/mu_p) Ip Wp | Rendered page 47 of NBC 105:2020 | Claude | 2026-10-07 |
| NBC 105:2020 Annex A materials and Annex B steel seismic rules (grades, sections, overstrength, connections, MRF/CBF checks) | NBC 105:2020 code text | Claude | 2026-10-07 |
| Seismic detailing basis is NBC 105:2020 Annex A (RC) and Annex B (steel), not IS 13920 / IS 800 Section 12 | NBC 105:2020 contents; DUDBC RCC checklist G.1 | Claude | 2026-10-07 |
| NBC 110:1994 = amendments to IS 456-1978; NBC 111:1994 = amendments to IS 800-1984 | NBC 110, NBC 111 forewords | Claude | 2026-10-07 |
| DUDBC RCC checklist uses IS 456:2000 and NBC 105:2020 Annex A | DUDBC checklist section G.1 | Claude | 2026-10-07 |
| Editions in user's library (NBC 103, 104, 106, 107, 108, 201, 205 are 1994; NBC 206 is 2024) | Document covers | Claude | 2026-10-07 |
| IS 456:2000 Table 5 (minimum grade, cement content, w/c by exposure) | archive.org OCR copy of IS 456:2000 | Claude | 2026-10-07 |
| IS 800:2007 Table 2 section classification limits; Amendment 1 bracing steel E250B / CVN > 27 J | archive.org OCR copy of IS 800:2007 | Claude | 2026-10-07 |
| NBC 205:2024 exists and replaces NBC 205:1994 | NBC 205:2024 foreword (municipal PDF, web) | Claude (secondary) | 2026-10-07 |
| IS 456:2000 36.4.2.1, 38.1 note, Annex G-1.1, 26.5.1.1 to 26.5.1.6, 26.5.2, 26.5.3.1, 23.2.1, Table 16, 26.2.1/26.2.1.1, 40.2.1.1, 40.2.2, 40.2.3.1, Table 18 (layout caveat) | archive.org OCR copy of IS 456:2000 | Claude | 2026-10-07 |
| IS 800:2007 Table 5, Table 7, Table 4 (layout caveat), Table 6 (layout caveat), 8.2.1.2/8.2.1.3 0.6Vd rule, 8.4.1 and 8.4.1.1 shear areas | archive.org OCR copy of IS 800:2007 | Claude | 2026-10-07 |
| IS 456:2000 Table 18, Table 19, Table 20, 26.2.1.1 (+25% compression), 40.4 | Page images, user's IS 456:2000 PDF (printed pp. 43, 68, 73) | Claude | 2026-10-07 |
| IS 800:2007 Table 4, Table 6, Table 10, Table 11, 6.2-6.4, 7.1.2.1, 8.2.1.2, 8.2.2, 9.3, Table 18, 10.3, 10.5.7; Table 9(a) reproduced by `calcs/is800_compression.py` | Page images, user's IS 800:2007 PDF (printed pp. 29, 31-34, 40, 44-45, 53-54, 71-72, 75, 79) | Claude | 2026-10-07 |
