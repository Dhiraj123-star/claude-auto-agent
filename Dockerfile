# ===== Stage 1: Builder =====
FROM python:3.12-slim AS builder

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# ===== Stage 2: Runtime =====
FROM python:3.12-slim

WORKDIR /app

COPY --from=builder /install /usr/local
COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
EXPOSE 8501

# Use Gunicorn + Uvicorn workers for FastAPI
CMD ["sh", "-c", "gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000 & streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]
