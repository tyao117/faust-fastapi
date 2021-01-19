from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import httpx

app = FastAPI()

class Item(BaseModel):
    name: str

@app.get("/")
async def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.post("/task")
async def send_task(payload: Item):
    r = httpx.post('http://fastapi-task:5000/new_task', data=payload)
    return {"status": "Okay"} if r.status_code == 200 else {"status": "Not Okay"}
