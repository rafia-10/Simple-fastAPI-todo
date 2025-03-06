from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


app = FastAPI()

 # Todo model
class Todo(BaseModel):
    title: str
    description: Optional[str]
    completed: bool = False


todos = []
# read everything
@app.get('todos', response_model=List[Todo])
def get_todos():
    return todos

# create
@app.post("/todos/", response_model=Todo)
def create_todo(todo: Todo):
    todos.append(todo)
    return todo

# Retrieve a specific to-do item by ID
@app.get("/todos/{id}", response_model=Todo)
def get_todo(id: int):
    if id < 0 or id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    return todos[id]


# update a task
@app.put("/todos/{id}", response_model=Todo)
def update_todo(id: int, updated_todo: Todo):
    if id < 0 or id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos[id] = updated_todo
    return updated_todo


# delete a task
@app.delete("/todos/{id}")
def delete_todo(id: int):
    if id < 0 or id >= len(todos):
        raise HTTPException(status_code=404, detail="Todo not found")
    todos.pop(id)
    return {"message": "Todo deleted successfully"}
