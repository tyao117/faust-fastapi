from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel

import httpx

app = FastAPI()

@app.post("/new_task")
async def new_task():
    return {"status": "Okay"}

@app.get("/new_task")
async def get_task():
    return {"status": "The task is working"} 

@app.get("/")
async def get_health():
    return {"status": "This service is up"}

