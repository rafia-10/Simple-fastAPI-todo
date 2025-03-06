from fastapi.testclient import TestClient
from main import app  # Import your FastAPI app

client = TestClient(app)

# 1 Test: Check if GET /todos returns an empty list initially
def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200  # HTTP 200 OK
    assert response.json() == []  # Should return an empty list initially

# 2 Test: Check if POST /todos adds a task successfully
def test_create_todo():
    new_task = {
        "title": "Test Task",
        "description": "This is a test task",
        "completed": False
    }
    response = client.post("/todos/", json=new_task)
    assert response.status_code == 200  # HTTP 200 OK
    assert response.json()["title"] == "Test Task"

# 3 Test: Check if GET /todos/{id} retrieves the correct task
def test_get_todo():
    # First, create a new task
    new_task = {
        "title": "Test Task 2",
        "description": "Another test task",
        "completed": False
    }
    post_response = client.post("/todos/", json=new_task)
    task_id = len(client.get("/todos").json()) - 1  # Get last task's index

    # Now, try to get the task by ID
    response = client.get(f"/todos/{task_id}")
    assert response.status_code == 200  # HTTP 200 OK
    assert response.json()["title"] == "Test Task 2"

# 4 Test: Check if updating a task works
def test_update_todo():
    updated_task = {
        "title": "Updated Task",
        "description": "Updated description",
        "completed": True
    }
    task_id = len(client.get("/todos").json()) - 1  # Get last task's index
    response = client.put(f"/todos/{task_id}", json=updated_task)
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Task"

# 5 Test: Check if DELETE /todos/{id} removes a task
def test_delete_todo():
    task_id = len(client.get("/todos").json()) - 1  # Get last task's index
    response = client.delete(f"/todos/{task_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted successfully"
