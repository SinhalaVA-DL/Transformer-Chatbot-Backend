from fastapi import Depends, FastAPI
from pydantic import BaseModel
from .routers import chat


app = FastAPI()

app.include_router(chat.router)


class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    response: str



@app.get("/")
async def root():
    return {"message": "Wellcome to the chatbot API"}