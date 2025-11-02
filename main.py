import os
from dotenv import load_dotenv
import autogen
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# Load .env
load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

if not api_key:
    raise RuntimeError("❗ Set ANTHROPIC_API_KEY in .env")

# Configure Claude Model for AutoGen
llm_config = {
    "model": "claude-haiku-4-5",
    "api_type": "anthropic",
    "api_key": api_key,
}

# Create Claude agent
assistant = autogen.AssistantAgent(
    name="claude_agent",
    llm_config=llm_config
)

def run():
    user_message = """
    Artificial intelligence is transforming industries by automating tasks,
    improving decision-making, and enabling personalized digital experiences.
    """
    
    reply = assistant.generate_reply(
        messages=[{"role": "user", "content": f"Summarize in 3 bullet points:\n{user_message}"}]
    )

    print("\n✅ Claude Response:\n")
    print(reply["content"])

if __name__ == "__main__":
    run()
