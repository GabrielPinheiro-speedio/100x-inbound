from fastapi import FastAPI
from contextlib import asynccontextmanager

from src.core.config import settings
from src.utils.logger import setup_logger, logger
from src.services.mongo_service import connect_to_mongo, close_mongo_connection
from src.services.es_service import connect_to_elastic, close_elastic_connection
from src.middlewares.auth_middleware import APITokenMiddleware
from src.api.v1.routes import router as v1_router

# Inicializa logger estruturado global
setup_logger()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Trata startup da aplicação
    logger.info(f"Iniciando {settings.project_name} - Modo: {settings.environment}")
    
    try:
        await connect_to_mongo()
    except Exception as e:
        logger.error(f"Erro ao conectar no banco Mongo: {e}")
        
    try:
        await connect_to_elastic()
    except Exception as e:
        logger.error(f"Erro ao conectar no Elasticsearch remoto: {e}")
        
    yield
    
    # Trata teardown
    await close_mongo_connection()
    await close_elastic_connection()

app = FastAPI(title=settings.project_name, lifespan=lifespan)

# Adicionando o middleware global de autenticação
app.add_middleware(APITokenMiddleware)

# Registrando roteadores
app.include_router(v1_router, prefix="/api/v1", tags=["Demo V1"])

@app.get("/health", tags=["Health"])
def health_check():
    """ Rota pública não protegida pelo header X-API-Token """
    return {"status": "ok"}
