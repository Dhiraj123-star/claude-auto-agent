import os
from dotenv import load_dotenv
import autogen
import warnings

# Ignore harmless model cost warnings
warnings.filterwarnings("ignore", category=UserWarning)

# Load API Key
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise RuntimeError("❗ Set ANTHROPIC_API_KEY in .env")

# Claude Model Configuration
llm_config = {
    "model": "claude-haiku-4-5",
    "api_type": "anthropic",
    "api_key": api_key,
}

# Create Agents
supervisor = autogen.AssistantAgent(name="supervisor", llm_config=llm_config)
worker = autogen.AssistantAgent(name="worker", llm_config=llm_config)

SUPERVISOR_SYSTEM = """
You are a supervisor agent. 
If the user's question requires short, direct explanation → answer it yourself.
If the user request involves summarization, rewriting, or extraction → delegate to the worker.
Respond with only one word FIRST: DIRECT or DELEGATE.
Then explain your reasoning briefly and (if delegating) give the task wording.
"""

WORKER_SYSTEM = """
You are a helper agent that performs concrete tasks such as summarization, rewriting,
bullet point extraction, and short structured outputs. Be concise.
"""

def decide_and_execute(user_msg: str):
    # Ask supervisor what to do
    decision = supervisor.generate_reply([
        {"role": "system", "content": SUPERVISOR_SYSTEM},
        {"role": "user", "content": user_msg},
    ])["content"]

    lines = decision.splitlines()
    mode = lines[0].strip().upper()

    # Extract task from rest of message
    task = "\n".join(lines[1:]).strip() or user_msg

    if mode == "DIRECT":
        # Supervisor answers directly
        final = supervisor.generate_reply([
            {"role": "system", "content": "Answer the user clearly and concisely."},
            {"role": "user", "content": user_msg},
        ])["content"]
        return "DIRECT", final

    else:
        # Worker performs task
        worker_result = worker.generate_reply([
            {"role": "system", "content": WORKER_SYSTEM},
            {"role": "user", "content": task},
        ])["content"]

        # Supervisor synthesizes final output
        final = supervisor.generate_reply([
            {"role": "system", "content": "Summarize and present to user clearly."},
            {"role": "user", "content": worker_result},
        ])["content"]

        return "DELEGATE", final

def tui():
    print("\n🤖 ClaudeAutoAgent (Supervisor + Worker)")
    print("Type `exit` to quit.\n")

    while True:
        user_msg = input("🧑 You: ").strip()
        if user_msg.lower() == "exit":
            print("\n👋 Goodbye!\n")
            break

        mode, reply = decide_and_execute(user_msg)

        print(f"\n🔧 Mode: {mode}")
        print("🤖 Claude:\n")
        print(reply, "\n")

if __name__ == "__main__":
    tui()
