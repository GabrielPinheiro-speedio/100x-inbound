import sys
import json
from loguru import logger

def setup_logger():
    """
    Configura o Loguru.
    """
    logger.remove()
    fmt = "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - <level>{message}</level> {extra}"
    logger.add(sys.stdout, format=fmt, level="INFO", enqueue=True)

def log_audit_event(event_type: str, user_target: str, context: dict = None):
    """
    Gera um log de auditoria estruturado. 
    Se a aplicação escalar, você consegue adicionar um 'sink' no loguru
    para enviar este JSON diretamente para o Elasticsearch ou DataDog.
    """
    if context is None:
        context = {}
        
    audit_logger = logger.bind(audit=True, event_type=event_type, target=user_target)
    audit_logger.info(f"AuditEvent: {event_type} - {json.dumps(context, ensure_ascii=False)}")
