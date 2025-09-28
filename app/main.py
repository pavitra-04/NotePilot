from typing import Annotated
from fastapi import FastAPI, Header, HTTPException
from pydantic import BaseModel

app = FastAPI()

@app.get("/greet/")
async def greet_user(name: str):
    return {"message": f"Hello {name}, welcome to NotePilot!"}
