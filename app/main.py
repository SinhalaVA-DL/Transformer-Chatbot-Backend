from fastapi import  FastAPI
from pydantic import BaseModel
from .routers import chat
from .routers import feedback
from fastapi.middleware.cors import CORSMiddleware
from app import config
from app.services.repository import get_mongo_meta,init_mongo



global_settings = config.get_settings()

app = FastAPI()

origins = [
    global_settings.client_origin,
]



# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"], # set to "*" to allow all origins or replace with a list of allowed origins
    allow_credentials=True,
    allow_methods=["*"], # set to "*" to allow all methods or replace with a list of allowed methods
    allow_headers=["*"], # set to "*" to allow all headers or replace with a list of allowed headers
)

app.include_router(chat.router)
app.include_router(feedback.router)


@app.on_event("startup")
async def startup_event():
    app.state.mongo_client, app.state.mongo_db, app.state.mongo_collection = await init_mongo(
        global_settings.db_name, global_settings.db_url, global_settings.collection,global_settings.collection2
    )


@app.get("/health-check")
async def health_check():
    return await get_mongo_meta()