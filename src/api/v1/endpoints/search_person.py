from fastapi import APIRouter, Request, Depends
from src.api.dependencies import get_db, get_es
from src.utils.logger import log_audit_event, logger

router = APIRouter()

@router.post("/search-person")
async def search_person(request: Request, db=Depends(get_db), es=Depends(get_es)):
    """
    Verifica o funcionamento do Skeleton.
    """
    log_audit_event(
        event_type="STATUS_CHECK",
        user_target="system",
        context={"ip": request.client.host}
    )
    
    logger.info("Verificando se serviços de banco estão instanciados...")
    
    return {
        "status": "online",
        "mongo_available": db is not None,
        "elasticsearch_available": es is not None
    }
