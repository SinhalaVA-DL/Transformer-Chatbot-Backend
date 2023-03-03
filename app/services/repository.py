import app.main as fastApp
from motor.motor_asyncio import AsyncIOMotorClient
from functools import lru_cache
from bson import ObjectId
from pymongo.errors import WriteError
from .exceptions import AlreadyExistsHTTPException

async def get_mongo_meta() -> dict:
    list_databases = await fastApp.app.state.mongo_client.list_database_names()
    list_of_collections = {}
    for db in list_databases:
        list_of_collections[db] = await fastApp.app.state.mongo_client[db].list_collection_names()
    mongo_meta = await fastApp.app.state.mongo_client.server_info()
    return {"version": mongo_meta["version"], "databases": list_databases, "collections": list_of_collections}


async def init_mongo(db_name: str, db_url: str, collection: str,collection2: str):
    """
    Args:
        db_name:
        db_url:
        collection:
    Returns:
    """
    mongo_client = AsyncIOMotorClient(db_url)
    mongo_database = mongo_client[db_name]
    mongo_collections = {
        collection: mongo_database.get_collection(collection),
        collection2: mongo_database.get_collection(collection2)
    }
    # return {0: mongo_client, 1: mongo_database, 2: mongo_collections}
    return mongo_client, mongo_database,mongo_collections





async def retrieve_document(document_id: str, collection: str) -> dict:
    """
 
    :param document_id:
    :param collection:
    :return:
    """

    if document := await fastApp.app.state.mongo_collection[collection].find_one({"_id": ObjectId(document_id)}, {'_id': 0}):
        return document
    else:
        raise ValueError(f"No document found for {document_id=} in {collection=}")


async def create_document(document: dict, collection: str) -> dict:
    """

    :param document:
    :param collection:
    :return:
    """
    try:
        document = await fastApp.app.state.mongo_collection[collection].insert_one(document)
        print(document.inserted_id)
        return await retrieve_document(document.inserted_id, collection)
    except WriteError:
        raise AlreadyExistsHTTPException(f"Document with {document.inserted_id=} already exists")
    


async def getAll_documents(collection: str):
          
    """
    :param collection:
    :return:
    """
    
    
    try :
        
        documents =  fastApp.app.state.mongo_collection[collection].find({}, {'_id': 0})
        my_data_as_list = await documents.to_list(length=100)
        for muted in my_data_as_list:
            print(muted)
        return my_data_as_list
    except WriteError: 
        raise ValueError(f"No documents found for {collection=}")
    
        


def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]


def serializeDict(a) -> dict:
    return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}