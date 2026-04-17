from fastapi import APIRouter
from src.api.v1.endpoints import status

api_router = APIRouter()

# Aqui você inclui as novas rotas conforme for criando os arquivos em endpoints/
api_router.include_router(status.router, prefix="/system", tags=["System"])

# Exemplo de como você faria para uma nova rota de usuários:
# from src.api.v1.endpoints import users
# api_router.include_router(users.router, prefix="/users", tags=["Users"])
