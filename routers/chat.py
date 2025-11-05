from fastapi import APIRouter
from pydantic import BaseModel
from agents import create_supervisor, create_worker

router = APIRouter()

supervisor = create_supervisor()
worker = create_worker()

SUPERVISOR_CONTEXT = (
    "You are a supervisor agent. Decide whether to answer directly "
    "or delegate to a worker for concrete tasks like summarization, extraction, or formatting.\n"
    "Respond with:\n"
    "DIRECT: <short reasoning>\n"
    "or\n"
    "DELEGATE: <task description for worker>"
)

class ChatRequest(BaseModel):
    message: str

class ChatResponse(BaseModel):
    mode: str
    result: str


def decide(user_text: str) -> tuple[str, str]:
    msg = [
        {"role": "system", "content": SUPERVISOR_CONTEXT},
        {"role": "user", "content": f"User message:\n{user_text}"},
    ]
    resp = supervisor.generate_reply(messages=msg)["content"].strip()
    first = resp.splitlines()[0].upper()
    rest = "\n".join(resp.splitlines()[1:]).strip()

    if first.startswith("DIRECT"):
        return "DIRECT", user_text
    else:
        return "DELEGATE", rest if rest else user_text


def worker_do(task: str) -> str:
    reply = worker.generate_reply(
        messages=[{"role": "user", "content": task}]
    )
    return reply["content"]


def supervisor_summarize(result: str, original: str) -> str:
    prompt = [
        {"role": "system", "content": "You summarize and clarify results returned from a worker."},
        {"role": "user", "content": (
            f"Worker result:\n{result}\n\n"
            f"Original question:\n{original}\n\n"
            "Give final, concise answer:"
        )},
    ]
    resp = supervisor.generate_reply(messages=prompt)
    return resp["content"]


@router.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    user_msg = req.message.strip()
    mode, task = decide(user_msg)

    if mode == "DIRECT":
        result = supervisor.generate_reply(
            messages=[{"role": "user", "content": user_msg}]
        )["content"]
        return ChatResponse(mode="DIRECT", result=result)

    else:
        worker_result = worker_do(task)
        final_answer = supervisor_summarize(worker_result, user_msg)
        return ChatResponse(mode="DELEGATE", result=final_answer)
