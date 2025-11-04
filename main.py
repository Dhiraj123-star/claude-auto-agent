from agents import supervisor, worker

def chat():
    print("\n🤖 ClaudeAutoAgent — TUI Chat Mode")
    print("💬 Type your message below.")
    print("🔚 Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit", "bye"]:
            print("\n👋 Goodbye!\n")
            break

        # First → Worker processes the request
        worker_reply = worker.generate_reply(
            messages=[{"role": "user", "content": user_input}]
        )["content"]

        # Then → Supervisor forms final answer based on worker output
        supervisor_reply = supervisor.generate_reply(
            messages=[
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": worker_reply}
            ]
        )

        print("\nClaude:\n" + supervisor_reply["content"] + "\n")


if __name__ == "__main__":
    chat()
