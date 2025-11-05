from fastapi import FastAPI
from routers.chat import router as chat_router

app = FastAPI(
    title="ClaudeAutoAgent API",
    description="Multi-Agent Supervisor + Worker system powered by Claude",
    version="1.0.0",
)

app.include_router(chat_router)

@app.get("/")
def home():
    return {"message": "ClaudeAutoAgent API is running 🚀"}
