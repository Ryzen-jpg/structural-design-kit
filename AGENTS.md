# Base44 Dev Environment

This repo is a **structural engineering knowledge toolkit** (markdown documents + Python calc scripts), not a traditional web app. To make it browsable in the preview, a small Flask viewer (`app.py`) was added.

## Running the app

```sh
docker compose -f docker-compose.base44.yml up -d
```

- Serves on port 3000
- Flask dev server with auto-reload (bind-mounted source)
- Scans the repo for `.md` files and renders them as HTML
- No external credentials or secrets needed

## Key files added for the viewer

- `app.py` — Flask app that renders markdown documents
- `templates/base.html` — layout template (sidebar + content)
- `static/style.css` — documentation viewer styling
- `requirements.txt` — Flask, Markdown, Pygments
- `docker-compose.base44.yml` — dev compose setup

## Notes

- The `jurisdication` branch has additional jurisdiction profile files (nepal.md, nepal-kathmandu.md, TEMPLATE.md) not present on this branch.
- The README references directories (`jurisdictions/`, `references/`, `checklists/`, `templates/`, `calcs/`) that don't exist on this branch — only root-level markdown files are present.
