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

# Claude model config
llm_config = {
    "model": "claude-haiku-4-5",   # change to sonnet/opus as needed
    "api_type": "anthropic",
    "api_key": api_key,
}

# Worker Agent → Generates coherent response
worker = autogen.AssistantAgent(
    name="worker_agent",
    llm_config=llm_config
)

# Supervisor Agent → Reads user's intent and delegates to worker
supervisor = autogen.AssistantAgent(
    name="supervisor_agent",
    system_message="You are a helpful assistant. Delegate all tasks to worker.",
    llm_config=llm_config
)
