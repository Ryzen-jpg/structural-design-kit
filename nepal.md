# Jurisdiction profile: Nepal

Checked against the user's NBC library on 2026-10-07 (see `references/nbc-library.md`).

## Code hierarchy

1. **Nepal National Building Code (NBC)** governs. In this kit, "NBC" always means the Nepal code.
2. **Indian Standards (IS)** apply where NBC refers to them or is silent, as is normal practice in Nepal.
3. No ACI, Eurocode, AS/NZS, AISC, ASCE, BS or other codes for design. A cross-check is allowed only when the user asks, labelled "outside Nepal design basis".
4. If NBC and IS conflict, NBC governs. Flag the conflict in the report.
5. Seismic design of buildings uses **NBC 105:2020** with its own detailing annexes: **Annex A (RC)** and **Annex B (steel)**. Do not use IS 1893. IS 13920 and IS 800 Section 12 are not the seismic detailing basis; Annex A and B are.

## IS edition conflict (read before every design)

NBC 110:1994 (Concrete) is written as Nepal amendments to **IS 456-1978** and says later IS 456 revisions do not apply
until NBC recognises them. NBC 111:1994 (Steel) is written as amendments to **IS 800-1984**.
Current permit practice uses the modern editions: the DUDBC "NBC Compliance Check List on Structural Analysis & Design for RCC"
lists **IS 456:2000** with NBC 105:2020 Annex A as the concrete design references.

Default in this kit: **IS 456:2000 and IS 800:2007 for member design, NBC 105:2020 for seismic loads and detailing.**
State this choice in the design basis report and confirm it with the permit authority. Where NBC 110 or 111 amends a
clause in a way that still applies, note it.

## Code map by design task

| Task | Governing document | Edition in user's library | Notes |
|---|---|---|---|
| Material unit weights | NBC 101 (DUDBC checklist cites it for densities) | not in library | Checklist cites NBC 101:1994 |
| Dead load | NBC 102 | not in library | IS 875 Part 1 if silent |
| Imposed (occupancy) load | NBC 103 | NBC 103:1994 | IS 875 Part 2 if silent |
| Wind | NBC 104 | NBC 104:1994 | IS 875 Part 3 if silent. DUDBC checklist allows omitting wind if seismic governs, with a note |
| Seismic, buildings | **NBC 105:2020** | NBC 105:2020 + commentary | Parameter sheet: `references/nbc-105-2020.md` |
| Snow | NBC 106 | NBC 106:1994 | |
| Fire safety | NBC 107 | NBC 107:1994 (provisional recommendation) | |
| Site / seismic hazard investigation | NBC 108 | NBC 108:1994 | Refers to IS 2720, IS 2974, IS 2911, IS 6403, IS 8009 and others |
| Concrete design | NBC 110 / IS 456 | NBC 110:1994 (IS 456-1978 amendments) | See conflict note above |
| Steel design | NBC 111 / IS 800 | NBC 111:1994 (IS 800-1984 amendments) | See conflict note above |
| Low-rise RC with masonry infill, rules of thumb | NBC 201 | NBC 201:1994 | |
| Low-rise RC without infill | NBC 205 | **NBC 205:1994 in library; NBC 205:2024 exists** | Get NBC 205:2024 before relying on it |
| Architectural requirements | NBC 206 | NBC 206:2024 | Egress, stairs, room sizes |
| Earthquake-resistant houses (non-engineered) | DUDBC Design Catalogue Vol I (2015) and Vol II (2017) | in library | Rural and reconstruction housing |
| Permit compliance | DUDBC RCC compliance checklist (NBC 105:2020) | in library | Fill it for every RC building permit |
| Concrete aids | SP 16, SP 34 | | |
| Reinforcement | IS 1786 | | NBC 105 Annex A limits grades (see reference sheet) |
| Structural steel | IS 2062, sections IS 808 | | NBC 105 Annex B allows only fy 250 and 345 MPa in seismic elements |
| Foundations | IS 1904, IS 6403, IS 8009, IS 2911 (piles), IS 2950 (rafts) | | Site investigation IS 1892, SPT IS 2131 |
| Masonry design | IS 1905 | | |
| Timber | IS 883 | | |
| Water-retaining structures | IS 3370 | | |

## Site overlays

- Kathmandu: `jurisdictions/nepal-kathmandu.md` (Z, soil class, spectrum, ground conditions, local items). Read it with this file for any Kathmandu project.

## Local practice notes

- Check which editions the municipality enforces and its permit drawing list (DUDBC list of minimum documents is in the library, in Nepali).
- Steel: check local availability of ISMB, ISHB, ISMC, ISA and plate grades before finalising sections.
- Rebar: confirm grade, elongation (> 15% for Fe 500 / Fe 550 per Annex A) and UTS/YS ratio (>= 1.15) on test certificates.
- Final drawings and calculations need review and sign-off per Nepal Engineering Council requirements.
