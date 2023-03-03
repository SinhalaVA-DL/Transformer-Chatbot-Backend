from pydantic import BaseModel, Field
from bson.objectid import ObjectId
from bson.errors import InvalidId

class ObjectIdField(str):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, value):
        try:
            return ObjectId(str(value))
        except InvalidId:
            raise ValueError("Not a valid ObjectId")
        

class ResponseBaseSchema(BaseModel):
    question: str
    chatbot_response: str
    user_response: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}


class ReactionBaseSchema(BaseModel):
    question: str
    chatbot_response: str
    reaction: str

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}




class ReactionResponse(ResponseBaseSchema):
    id: ObjectIdField = Field(...)