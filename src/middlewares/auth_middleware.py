from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from src.core.config import settings
from src.utils.logger import logger

class APITokenMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Excluir rotas públicas e documentação do API Token
        if request.url.path in ["/docs", "/redoc", "/openapi.json", "/health"]:
            return await call_next(request)

        token = request.headers.get("X-API-Token")
        
        if not token or token != settings.api_token:
            logger.warning(f"Acesso bloqueado pelo Auth Middleware. IP: {request.client.host}")
            return JSONResponse(
                status_code=401,
                content={"detail": "Acesso não autorizado. Header X-API-Token inválido ou ausente."}
            )

        response = await call_next(request)
        return response
