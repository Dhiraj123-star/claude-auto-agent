from fastapi import APIRouter
from agents import create_worker, create_supervisor

router = APIRouter(prefix="/chat")

@router.post("/")
async def chat_endpoint(message: str):
    supervisor = create_supervisor()
    worker = create_worker()

    # Send only one message turn
    reply = supervisor.generate_reply(
        messages=[{"role": "user", "content": message}]
    )

    return {"response": reply["content"]}
