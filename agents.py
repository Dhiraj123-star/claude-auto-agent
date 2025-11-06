import os
from dotenv import load_dotenv
import autogen
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("❗ Set ANTHROPIC_API_KEY in .env")

llm_config = {
    "model": "claude-haiku-4-5",
    "api_type": "anthropic",
    "api_key": api_key,
}

def create_worker():
    return autogen.AssistantAgent(
        name="worker_agent",
        llm_config=llm_config
    )

def create_supervisor():
    return autogen.AssistantAgent(
        name="supervisor_agent",
        system_message="You are a helpful assistant. Respond directly to the user.",
        llm_config=llm_config
    )
