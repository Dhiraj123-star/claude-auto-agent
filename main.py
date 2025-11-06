from fastapi import FastAPI
from routers.chat import router as chat_router

app = FastAPI(title="Claude Auto Agent API")

app.include_router(chat_router)

@app.get("/")
def root():
    return {"message": "Claude Auto Agent Running ✅"}
