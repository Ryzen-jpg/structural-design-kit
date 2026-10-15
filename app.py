import os
import markdown
from flask import Flask, render_template, abort, Response

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
    # Prefer README.md as the default document
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)
