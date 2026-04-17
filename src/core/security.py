from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader
from src.core.config import settings

# Define o header esperado
api_key_header = APIKeyHeader(name="X-API-Token", auto_error=True)

def verify_api_token(api_key_header: str = Security(api_key_header)):
    if api_key_header != settings.api_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token de API inválido",
        )
    return api_key_header
