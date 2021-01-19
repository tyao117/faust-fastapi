from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
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
    payload = jsonable_encoder(payload)
    r = httpx.post("http://fastapi-task/new_task", json=payload)
    return r


@app.get("/task")
async def get_task():
    r = httpx.get("http://fastapi-task/new_task")
    json_response = r.json()
    return json_response if json_response else {"Status": "it did not work as intended"}
