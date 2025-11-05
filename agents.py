import os
from dotenv import load_dotenv
import autogen
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

# Load API Key
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("❗ Set ANTHROPIC_API_KEY in .env")

# Shared Claude config
llm_config = {
    "model": "claude-haiku-4-5",
    "api_type": "anthropic",
    "api_key": api_key,
}


def create_worker():
    """Return a Worker Agent (does concrete tasks)."""
    return autogen.AssistantAgent(
        name="worker_agent",
        llm_config=llm_config
    )


def create_supervisor():
    """Return a Supervisor Agent (decides & delegates)."""
    return autogen.AssistantAgent(
        name="supervisor_agent",
        system_message=(
            "You are a supervisor agent. Decide if you should answer directly "
            "or delegate to the worker for summarization, transformation, or extraction tasks."
        ),
        llm_config=llm_config
    )
