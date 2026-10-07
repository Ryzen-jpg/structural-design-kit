# Structural design kit

A version-controlled skill and toolkit for structural design decisions: any structure type,
any material, with code systems kept in swappable jurisdiction profiles. Nepal (NBC + Indian
Standards) is the default profile.

## Layout

```
SKILL.md            Core workflow and rules (load this as the skill)
jurisdictions/      Code hierarchy per country. nepal.md is the default; TEMPLATE.md to add others
references/         Code quick references, each with edition and verification status
checklists/         Required inputs, element checklists, STAAD setup, review
templates/          Design basis report and project brief templates
calcs/              Python hand-check scripts with tests
VERIFY.md           Every value still taken from memory, to be checked against code text
CHANGELOG.md        What changed and why
```

## Rules for contributing

1. Every code value in `references/` carries its source: code, edition, clause, and "verified" or "(verify)".
2. When you check a value against the code text, update `VERIFY.md` and the reference file in the same commit.
3. Calc scripts need a worked example as a test. Run `python -m pytest calcs` before committing.
4. Project data (grids, loads, soil reports, client names) does not go in this repo.
5. Code PDFs are linked, not committed, unless redistribution is confirmed to be allowed.

## Using it as a skill

Copy or link the repo folder into your skills directory, or upload `SKILL.md` with its folder.
The skill reads `jurisdictions/`, `checklists/` and `references/` as needed.

## Disclaimer

This kit supports engineering work. It does not replace the code text or the judgement and
sign-off of a licensed engineer.
