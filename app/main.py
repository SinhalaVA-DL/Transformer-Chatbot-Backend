from fastapi import  FastAPI
from pydantic import BaseModel
from .routers import chat
from .routers import feedback

app = FastAPI()

app.include_router(chat.router)
app.include_router(feedback.router)



@app.get("/")
async def root():
    return {"message": "Wellcome to the chatbot API"}