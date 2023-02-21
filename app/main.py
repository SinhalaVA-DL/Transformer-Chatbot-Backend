from fastapi import  FastAPI
from pydantic import BaseModel
from .routers import chat
from .routers import feedback
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000/"], # set to "*" to allow all origins or replace with a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"], # set to "*" to allow all methods or replace with a list of allowed methods
    allow_headers=["*"], # set to "*" to allow all headers or replace with a list of allowed headers
)

app.include_router(chat.router)
app.include_router(feedback.router)



@app.get("/")
async def root():
    return {"message": "Wellcome to the chatbot API"}