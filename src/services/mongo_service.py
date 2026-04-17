from motor.motor_asyncio import AsyncIOMotorClient
from src.core.config import settings
from src.utils.logger import logger

class MongoDB:
    client: AsyncIOMotorClient = None

db = MongoDB()

async def connect_to_mongo():
    logger.info("Conectando ao MongoDB...")
    db.client = AsyncIOMotorClient(settings.mongo_url)
    logger.info("MongoDB conectado com sucesso")

async def close_mongo_connection():
    if db.client:
        logger.info("Fechando conexão com MongoDB")
        db.client.close()

def get_database():
    return db.client.get_default_database() if db.client else None
