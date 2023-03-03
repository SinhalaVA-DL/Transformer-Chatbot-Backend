from fastapi import APIRouter,status,HTTPException
from pydantic import BaseModel
from ..schemas import schemas
from ..services.repository import retrieve_document , create_document, getAll_documents
from ..services.exceptions import NotFoundHTTPException
from fastapi.encoders import jsonable_encoder
from app import config


global_settings = config.get_settings()
collection = global_settings.collection
collection2 = global_settings.collection2

router = APIRouter()

@router.post("/feedback/create-rate", tags=["feedback"])
async def rate_response(payload:schemas.ReactionBaseSchema):

    try:
        payload = jsonable_encoder(payload)
        return await create_document(payload, collection2)
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))


@router.post("/feedback/create-response", tags=["feedback"])
async def create_response(payload: schemas.ResponseBaseSchema):

    try:
        payload = jsonable_encoder(payload)
        return await create_document(payload, collection)
    except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))
    


@router.get("/feedback/get-all-responses", tags=["feedback"])
async def get_responses():

   try:
        response = await getAll_documents(collection)
        return response
   except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))
    
@router.get("/feedback/get-all-reactions", tags=["feedback"])
async def get_requests():

   try:
        response = await getAll_documents(collection2)
        return response
   except ValueError as exception:
        raise NotFoundHTTPException(msg=str(exception))