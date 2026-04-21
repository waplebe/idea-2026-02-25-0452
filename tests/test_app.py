import pytest
from fastapi.test import TestClient
from app import app

@pytest.fixture
def test_client():
    client = TestClient(app)
    return client

def test_read_tasks():
    response = test_client.get("/tasks")
    assert response.status_code == 200
    assert response.json() == []  # Expect an empty list initially

def test_create_task():
    response = test_client.post("/tasks", json={"title": "Test Task", "description": "Test Description"})
    assert response.status_code == 201
    assert response.json()["title"] == "Test Task"
    assert response.json()["description"] == "Test Description"

def test_read_task():
    # Create a task first
    response = test_client.post("/tasks", json={"title": "Existing Task", "description": "Existing Description"})
    task_id = response.json()["id"]

    response = test_client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["id"] == task_id
    assert response.json()["title"] == "Existing Task"
    assert response.json()["description"] == "Existing Description"

def test_update_task():
    # Create a task first
    response = test_client.post("/tasks", json={"title": "Initial Task", "description": "Initial Description"})
    task_id = response.json()["id"]

    # Update the task
    response = test_client.put(f"/tasks/{task_id}", json={"title": "Updated Task", "description": "Updated Description"})
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["title"] == "Updated Task"
    assert updated_task["description"] == "Updated Description"

    # Verify the update
    response = test_client.get(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"
    assert response.json()["description"] == "Updated Description"

def test_delete_task():
    # Create a task first
    response = test_client.post("/tasks", json={"title": "Delete Task", "description": "Delete Description"})
    task_id = response.json()["id"]

    # Delete the task
    response = test_client.delete(f"/tasks/{task_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Task deleted"}

    # Verify the deletion
    response = test_client.get(f"/tasks/{task_id}")
    assert response.status_code == 404