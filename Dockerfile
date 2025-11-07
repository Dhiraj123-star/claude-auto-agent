# ===== Stage 1: Builder =====
FROM python:3.12-slim AS builder

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential curl && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install --prefix=/install -r requirements.txt

# ===== Stage 2: Runtime =====
FROM python:3.12-slim

WORKDIR /app

# Copy installed Python packages
COPY --from=builder /install /usr/local

# Copy source code
COPY . .

# Environment
ENV PYTHONUNBUFFERED=1

EXPOSE 8000
EXPOSE 8501

CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port=8501 --server.address=0.0.0.0"]
