from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import sqlite3
from database.create_tables import create_tables

DATABASE_URL = "sqlite:///tasks.db"

app = FastAPI()

# Database models
class Task(BaseModel):
    id: int
    title: str
    description: str

# Database connection
def get_db():
    db = sqlite3.connect(DATABASE_URL)
    db.row_factory = sqlite3.Row
    return db

# API endpoints
@app.on_event("startup")
async def startup_event():
    db = get_db()
    db.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT NOT NULL, description TEXT)")
    db.commit()

@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    db = get_db()
    tasks = db.execute("SELECT * FROM tasks").fetchall()
    return [Task(**row) for row in tasks]

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    db = get_db()
    db.execute("INSERT INTO tasks (title, description) VALUES (?, ?)", (task.title, task.description))
    db.commit()
    task_id = db.execute("SELECT last_insert_rowid()").fetchone()[0]
    return Task(id=task_id, title=task.title, description=task.description)

@app.get("/tasks/{id}", response_model=Task)
async def read_task(id: int):
    db = get_db()
    task = db.execute("SELECT * FROM tasks WHERE id = ?", (id,)).fetchone()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return Task(**task)

@app.put("/tasks/{id}", response_model=Task)
async def update_task(id: int, task: Task):
    db = get_db()
    db.execute("UPDATE tasks SET title = ?, description = ? WHERE id = ?", (task.title, task.description, id))
    db.commit()
    updated_task = db.execute("SELECT * FROM tasks WHERE id = ?", (id,)).fetchone()
    return Task(**updated_task)

@app.delete("/tasks/{id}")
async def delete_task(id: int):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (id,))
    db.commit()
    return {"message": "Task deleted"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)