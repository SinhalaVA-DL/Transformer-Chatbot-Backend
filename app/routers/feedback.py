from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class RateIn(BaseModel):
    rate: int

class UserAnswer(BaseModel):
    answer: str



@router.post("/feedback/rate", tags=["feedback"])
async def rate_response(payload: RateIn):

    response = 'You have Rated ' + payload.rate
    return {"resonse": response}


@router.post("/feedback/user-answer", tags=["feedback"])
async def user_answer(payload: UserAnswer):

    response = 'Thank you for your Response'
    return {"resonse": response}