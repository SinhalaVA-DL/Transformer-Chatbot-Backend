from fastapi import APIRouter
from ..internal.model.chatbot import predictor
from ..internal.result import get_result
from pydantic import BaseModel

router = APIRouter()

class TextIn(BaseModel):
    text: str


class PredictionOut(BaseModel):
    response: str



@router.get("/chat/health", tags=["chat"])
async def health():
    return {"health_check": "OK"}


@router.post("/chat/ask", tags=["chat"])
async def predict(payload: TextIn):

    # response = predictor.predict(payload.text)
    response = get_result(payload.text)
    return {"response": response}