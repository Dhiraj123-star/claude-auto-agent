FROM python:3.12-slim

WORKDIR /app

# Install deps
RUN apt-get update && apt-get install -y --no-install-recommends \
    nginx supervisor build-essential && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . .
COPY nginx.conf /etc/nginx/nginx.conf

# Supervisor to run multiple processes
COPY <<EOF /etc/supervisor/conf.d/app.conf
[supervisord]
nodaemon=true

[program:api]
command=gunicorn main:app --workers 4 --worker-class uvicorn.workers.UvicornWorker --bind 0.0.0.0:%(ENV_PORT)s

[program:ui]
command=streamlit run app.py --server.baseUrlPath=/ui --server.port=8501 --server.address=0.0.0.0

[program:nginx]
command=nginx -g "daemon off;"
EOF

ENV PYTHONUNBUFFERED=1
EXPOSE 8000
EXPOSE 8501

CMD ["/usr/bin/supervisord"]
