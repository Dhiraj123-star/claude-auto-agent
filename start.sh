#!/usr/bin/env bash

# Start FastAPI via Gunicorn
gunicorn main:app \
  --workers 4 \
  --worker-class uvicorn.workers.UvicornWorker \
  --bind 0.0.0.0:8000 &

# Start Streamlit UI
streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &

# Wait so container doesn't exit
wait -n
