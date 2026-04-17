FROM python:3.11-slim

# Definir diretório de trabalho
WORKDIR /app

# Instalar dependências de sistema necessárias
RUN apt-get update && apt-get install -y curl gcc && rm -rf /var/lib/apt/lists/*
RUN pip install "poetry==1.8.2"

# Copiar arquivos de dependência 
COPY pyproject.toml poetry.lock* ./

# Evitar a criação de virtualenv dentro do container e instalar
RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi --no-root

# Copiar estrutura do site
COPY . .

# Expõe a porta 8000
EXPOSE 8000

# Executar a aplicação
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
