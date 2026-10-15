"""SQLite database operations for structural design tasks."""

import os
import sqlite3

DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "tasks.db")


def get_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            project TEXT DEFAULT '',
            task_type TEXT NOT NULL,
            template_id TEXT NOT NULL,
            status TEXT DEFAULT 'pending',
            notes TEXT DEFAULT '',
            items_json TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()


def get_all_tasks():
    conn = get_db()
    tasks = conn.execute("SELECT * FROM tasks ORDER BY created_at DESC").fetchall()
    conn.close()
    return tasks


def get_task(task_id):
    conn = get_db()
    task = conn.execute("SELECT * FROM tasks WHERE id = ?", (task_id,)).fetchone()
    conn.close()
    return task


def create_task(title, project, task_type, template_id, items_json, notes=""):
    conn = get_db()
    cursor = conn.execute(
        "INSERT INTO tasks (title, project, task_type, template_id, items_json, notes) "
        "VALUES (?, ?, ?, ?, ?, ?)",
        (title, project, task_type, template_id, items_json, notes),
    )
    conn.commit()
    task_id = cursor.lastrowid
    conn.close()
    return task_id


def update_task(task_id, title, project, status, notes, items_json):
    conn = get_db()
    conn.execute(
        "UPDATE tasks SET title = ?, project = ?, status = ?, notes = ?, "
        "items_json = ?, updated_at = CURRENT_TIMESTAMP WHERE id = ?",
        (title, project, status, notes, items_json, task_id),
    )
    conn.commit()
    conn.close()


def delete_task(task_id):
    conn = get_db()
    conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
