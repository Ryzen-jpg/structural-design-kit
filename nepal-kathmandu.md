# Site profile: Kathmandu (overlay on `nepal.md`)

Use together with `jurisdictions/nepal.md`. Everything there still applies: NBC governs, Indian Standards fill gaps,
no other codes unless a labelled cross-check is requested, NBC 105:2020 for seismic loads and detailing.
This file adds what is fixed by the Kathmandu location.

Checked 2026-10-07 against the user's copies of NBC 105:2020 (111 pages) and NBC 108:1994, text extracted from the PDFs.
Spectrum and coefficient numbers were computed with `calcs/nbc105_esm.py`.

## Scope

- Applies to Kathmandu: Table 4-5 lists it with Z = 0.35, and Table 4-4 lists it as a Type D soil site.
- Table 4-4 lists six municipalities as Type D: Kathmandu, Lalitpur, Bhaktapur, Madhyapur Thimi, Kageshori Manohara (code spelling), Tokha.
- Lalitpur, Bhaktapur, Madhyapur Thimi, Kageshori Manohara and Tokha are not in Table 4-5. Read Z for them from the zoning map
  (Figure 4-3; the text of 4.1.4 calls it Figure 4-4, which is a misprint). Do not assume it equals Kathmandu's.
- Any other municipality inside the Valley: 4.1.3.4 says Valley sites are taken from Table 4-4, and the text does not say what to do for
  a municipality that is not listed. Confirm the class with the permit authority and the site investigation (open item in `VERIFY.md`).

## Fixed seismic parameters

| Parameter | Value | Source |
|---|---|---|
| Zone factor Z | 0.35 | NBC 105:2020 Table 4-5 |
| Soil type | D (very soft) | 4.1.3.4, Table 4-4 |
| Ta | 0.5 s for MRSM; 0 for ESM | Table 4-1 and its footnote |
| Tc | 2.0 s | Table 4-1 |
| alpha | 2.25 | Table 4-1 |
| K | 0.8 | Table 4-1 |
| Importance factor I | by use, not by location: 1.0 / 1.25 / 1.5 | Table 4-6 |
| SLS spectrum | Cs = 0.20 C | 4.2 |

## Design spectrum for I = 1.0

C(T) = Ch(T) x Z x I. Multiply every value by I for other importance classes.

| T (s) | C, ESM (Ta = 0) | C, MRSM |
|---|---|---|
| 0 | 0.7875 | 0.3500 |
| 0.1 | 0.7875 | 0.4375 |
| 0.2 | 0.7875 | 0.5250 |
| 0.3 | 0.7875 | 0.6125 |
| 0.5 to 2.0 | 0.7875 | 0.7875 |
| 2.5 | 0.4677 | 0.4677 |
| 3.0 | 0.3111 | 0.3111 |
| 4.0 | 0.1673 | 0.1673 |
| 6.0 | 0.0719 | 0.0719 |

Design base shear coefficient at I = 1.0, T within the plateau (hand-check anchor for the STAAD base shear, V = Cd W):

| System | Cd, ULS = C / (Rmu x Omega_u) | Cd, SLS = Cs / Omega_s |
|---|---|---|
| Steel MRF, RC MRF | 0.13125 | 0.126 |
| Dual RC shear wall | 0.16071 | 0.13125 |

For any other system take Rmu, Omega_u and Omega_s from Table 5-2 (`references/nbc-105-2020.md`).

## What this means for design choices (kit guidance, not code text)

- The ESM coefficient is constant from T = 0 to 2.0 s. A more flexible building gets no force reduction from a longer period
  until T exceeds 2.0 s, and V = Cd W, so every kN of seismic weight removed lowers base shear one for one.
  Put floor, wall and roof weight in the system comparison (SKILL.md step 3), together with cost and buildability.
- If the combined MRSM base shear VR is below the ESM base shear V, MRSM results are multiplied by V/VR (7.5), so MRSM base shear is never below the ESM value.
- Check the period used: lesser of the Rayleigh period and the amplified empirical period (5.1).

## Ground conditions

Table 4-4 fixes the seismic soil class. It does not give bearing capacity, settlement or groundwater. The code text on the ground itself:

- NBC 105:2020 2.3.2: the standard's seismic forces assume soil that does not settle, liquefy or slide in an earthquake.
- NBC 105:2020 2.3.3: where the soil is soft and prone to liquefaction or lateral spreading, the foundation design must account for the
  soil movement, deep (pile) foundations are normally preferred, and advice from a geotechnical expert is to be sought.
- NBC 108:1994 3.2: sites on ancient lake deposits, with the Kathmandu Valley named as the example, shall be investigated for liquefaction
  susceptibility, and mitigation taken to minimise the risk. For the liquefaction analysis a 20 m exploration depth should suffice (NBC 108 4.3).
- NBC 105 Commentary: the Type D class represents the very soft deep clay deposit of the Valley core.

Neither NBC 105 nor NBC 108 gives a screening method or thresholds for liquefaction. Do not invent one. Ask for the geotechnical report and
the method it used, and cite the standard that method comes from. Required from the site investigation before foundation design:

- allowable bearing pressure and settlement at the proposed founding level (NBC 108 4.4 and the IS methods in `nepal.md`);
- groundwater level and its seasonal variation, and the uplift and dewatering consequences for any basement or raft (IS 2950);
- the liquefaction assessment, covering at least 20 m depth.

## Local practice notes (all open, none verified)

- Permit authority: confirm which editions of NBC 105, NBC 110/111 and IS 456 / IS 800 the Kathmandu office enforces. Track in `VERIFY.md`.
- Building bylaws (height, setbacks, ground coverage, floor area ratio, parking, fire access) are set by the municipality and are
  not in the library. Read the current bylaw for the ward and road width. Do not use numbers from memory.
- Heritage and monument zones in the Valley can restrict height and form. Check the plot against the municipality's heritage map.
- Site access: narrow lanes limit crane, concrete pump and long steel member delivery. Include this under buildability when
  comparing steel and RC.
- Final drawings and calculations need review and sign-off per Nepal Engineering Council requirements.

## Sources

- NBC 105:2020 Seismic Design of Buildings in Nepal: 2.3.2, 2.3.3, 4.1.3.4, 4.1.4, 4.2, 5.1, 7.5, Tables 4-1, 4-4, 4-5, 4-6, Figure 4-3, and its Commentary
- NBC 108:1994 Site Consideration for Seismic Hazards: 3.2, 4.3, 4.4
- Other documents: see the code map in `jurisdictions/nepal.md`
