from elasticsearch import AsyncElasticsearch
from src.core.config import settings
from src.utils.logger import logger

class ESHook:
    client: AsyncElasticsearch = None

es = ESHook()

async def connect_to_elastic():
    logger.info(f"Conectando ao Elasticsearch remoto na URl: {settings.elasticsearch_url}...")
    es.client = AsyncElasticsearch(settings.elasticsearch_url)
    try:
        # Tenta um "ping" para ver se está de pé
        await es.client.info()
        logger.info("Elasticsearch conectado com sucesso!")
    except Exception as e:
        logger.error(f"Não foi possível conectar ao Elasticsearch (ele pode estar fora via nuvem). Detalhe: {e}")

async def close_elastic_connection():
    if es.client:
        logger.info("Fechando conexão com Elasticsearch")
        await es.client.close()

def get_es_client():
    return es.client
