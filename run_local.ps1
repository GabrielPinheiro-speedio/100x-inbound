# Script prático para rodar a API localmente fora do docker, mantendo o hot-reload
Write-Host "Iniciando a API FastAPI localmente..." -ForegroundColor Green

# Se você usar virtualenv via poetry:
# poetry run uvicorn src.main:app --reload

# Módulo padrao se rodar global na máquina com as pip dependencies:
python -m uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
