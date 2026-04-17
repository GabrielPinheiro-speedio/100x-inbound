from fastapi import Request
from src.services.mongo_service import get_database
from src.services.es_service import get_es_client

async def get_db():
    return get_database()

async def get_es():
    return get_es_client()
