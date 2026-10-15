import os
import json
import markdown
from flask import Flask, render_template, abort, request, redirect, url_for, Response

from db import init_db, get_all_tasks, get_task, create_task as db_create, update_task as db_update, delete_task as db_delete
from design_templates import TEMPLATES

app = Flask(__name__)
REPO_ROOT = os.path.dirname(os.path.abspath(__file__))

DISPLAY_NAMES = {
    "README.md": "Overview",
    "SKILL.md": "Workflow & Rules",
    "VERIFY.md": "Verification Log",
    "CHANGELOG.md": "Changelog",
    "AGENTS.md": "Dev Environment",
}

EXCLUDE_DIRS = {".git", "__pycache__", ".pytest_cache", "node_modules", ".base44"}


# ── Markdown document viewer ──

def get_markdown_files():
    """Recursively find all .md files in the repo, excluding build/cache dirs."""
    files = []
    for root, dirs, filenames in os.walk(REPO_ROOT):
        dirs[:] = [d for d in dirs if d not in EXCLUDE_DIRS]
        for name in filenames:
            if name.endswith(".md"):
                relpath = os.path.relpath(os.path.join(root, name), REPO_ROOT)
                files.append(relpath)
    files = sorted(files)
    if "README.md" in files:
        files.remove("README.md")
        files.insert(0, "README.md")
    return files


def display_name(filepath):
    if filepath in DISPLAY_NAMES:
        return DISPLAY_NAMES[filepath]
    return os.path.splitext(filepath)[0]


def render_md(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        text = f.read()
    return markdown.markdown(
        text,
        extensions=["tables", "fenced_code", "codehilite", "toc", "sane_lists"],
    )


def _render(filename, files):
    filepath = os.path.join(REPO_ROOT, filename)
    if not filename.endswith(".md") or not os.path.isfile(filepath):
        abort(404)
    return render_template(
        "document.html",
        files=files,
        active=filename,
        title=display_name(filename),
        content=render_md(filepath),
    )


@app.route("/")
def index():
    files = get_markdown_files()
    if not files:
        return render_template(
            "document.html",
            files=[],
            active=None,
            title="No documents",
            content="<p>No markdown files found.</p>",
        )
    return _render(files[0], files)


@app.route("/doc/<path:filename>")
def view_doc(filename):
    return _render(filename, get_markdown_files())


@app.route("/pygments.css")
def pygments_css():
    from pygments.formatters import HtmlFormatter
    css = HtmlFormatter(style="friendly").get_style_defs(".codehilite")
    return Response(css, mimetype="text/css")


# ── Task management ──

def _task_progress(items_json):
    """Return 'done/total' string for a task's items."""
    try:
        items = json.loads(items_json)
    except (json.JSONDecodeError, TypeError):
        return "—"
    checks = [i for i in items if i.get("type") == "check"]
    fields = [i for i in items if i.get("type") == "field"]
    if checks:
        done = sum(1 for i in checks if i.get("checked"))
        return f"{done}/{len(checks)}"
    if fields:
        done = sum(1 for i in fields if i.get("value"))
        return f"{done}/{len(fields)}"
    return "—"


@app.route("/tasks")
def tasks():
    init_db()
    all_tasks = get_all_tasks()
    progress = {t["id"]: _task_progress(t["items_json"]) for t in all_tasks}
    return render_template("tasks.html", tasks=all_tasks, progress=progress)


@app.route("/tasks/new")
def new_task():
    return render_template(
        "new_task.html", templates=TEMPLATES, templates_json=json.dumps(TEMPLATES)
    )


@app.route("/tasks/create", methods=["POST"])
def create_task_route():
    template_id = request.form["template_id"]
    template = next((t for t in TEMPLATES if t["id"] == template_id), None)
    if not template:
        abort(404)
    title = request.form["title"]
    project = request.form.get("project", "")
    notes = request.form.get("notes", "")
    items_json = json.dumps(template["items"])
    task_id = db_create(title, project, template["type"], template_id, items_json, notes)
    return redirect(url_for("task_detail", task_id=task_id))


@app.route("/tasks/<int:task_id>")
def task_detail(task_id):
    init_db()
    task = get_task(task_id)
    if not task:
        abort(404)
    return render_template("task_detail.html", task=task)


@app.route("/tasks/<int:task_id>/update", methods=["POST"])
def update_task_route(task_id):
    title = request.form["title"]
    project = request.form.get("project", "")
    status = request.form["status"]
    notes = request.form.get("notes", "")
    items_json = request.form["items_json"]
    db_update(task_id, title, project, status, notes, items_json)
    return redirect(url_for("task_detail", task_id=task_id))


@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task_route(task_id):
    db_delete(task_id)
    return redirect(url_for("tasks"))


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=3000, debug=True)
