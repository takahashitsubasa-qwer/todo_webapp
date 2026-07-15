# source .venv/bin/activate
# deactivate
# uvicorn test:app --reload

# git add .
# git commit -m "変更内容"
# git push


from pydantic import BaseModel
from fastapi import FastAPI
from enum import Enum
from sqlite.database import *

createdb()

class Priority(str,Enum):
    high = "high"
    middle = "middle"
    low = "low"

class Title(BaseModel):
    title_content: str
    priority: Priority
    done: bool = False

app = FastAPI()

@app.get("/todos")
async def get_todo():
    raw_data = getdb()
    todo_list= []
    for row in raw_data:
        todo_list.append({
            "todo_id": row[0],
            "title_content": row[1],
            "priority": row[2],
            "done": bool(row[3])
        })
    return todo_list


@app.post("/todos")
async def post_todo(todopost:Title):
    one_of_todo = (todopost.title_content,todopost.priority,todopost.done)

    postdb(one_of_todo)
    return {"title_content": todopost.title_content, "priority": todopost.priority, "done": todopost.done}
 

@app.put("/todos/{todo_put_id}")
async def put_todo(todo_put_id: int,todoput:Title):

    todo_put_list=[todoput.title_content,todoput.priority,todo_put_id]

    putdb(todo_put_list)

@app.delete("/todos/{todo_delete_id}")
async def delete_todo(todo_delete_id: int):
    for n_delete in todos:
        if n_delete["todo_id"] == todo_delete_id:
            todos.remove(n_delete)
            return{"message":"sakujo"}

@app.patch("/todos/{todo_patch_id}/done")
async def patch_todo(todo_patch_id: int):
    for n_patch in todos:
        if n_patch["todo_id"] == todo_patch_id:
            n_patch["done"] = True