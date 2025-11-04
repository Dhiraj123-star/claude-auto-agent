
# 🤖 ClaudeAutoAgent — TUI Edition

A simple **agentic AI console application** built using **Microsoft AutoGen** and **Anthropic Claude**, now enhanced with a **TUI (Terminal User Interface)**.

This version uses a **Supervisor → Worker** collaborative agent approach and allows you to **chat interactively in the terminal**.

---

## ✨ Features

* **Interactive TUI chat mode** (type messages, get Claude responses)
* **Two-agent setup:**

  * **Supervisor Agent:** Interprets your request
  * **Worker Agent:** Executes reasoning + generates response
* Runs fully in **terminal**, no UI libraries required
* Uses **Claude (Anthropic API)** models
* Clean, minimal, extendable code

---

## 🛠️ Tech Stack

| Component         | Purpose             |
| ----------------- | ------------------- |
| **Python 3.10+**  | Runtime             |
| **autogen**       | Agent orchestration |
| **anthropic API** | Claude model access |
| **python-dotenv** | API key management  |

---

## 📦 Setup Instructions

### 1️⃣ Clone the Project

```bash
git clone <your-repo-url>
cd ClaudeAutoAgent
```

### 2️⃣ Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4️⃣ Add Your Claude API Key

Create a `.env` file in the project directory:

```
ANTHROPIC_API_KEY=your_real_claude_api_key_here
```

---

## 🚀 Run the TUI Agent

Start chat mode:

```bash
python main.py
```

When the program runs, you'll enter **interactive mode**:

```
💬 Type anything to ask Claude.
🔚 Type 'exit' to quit.

You: 
```

Example:

```
You: explain event-driven architecture in simple terms
Claude (via agents): ...
```

---

## 🎨 How It Works (Architecture)

```
You (Terminal)
    ↓
Supervisor Agent  (interprets user intent)
    ↓
Worker Agent      (generates response using Claude)
    ↓
Response shown in terminal
```

---

## 🧩 Extend the Agents

| Feature              | How to Add                         |
| -------------------- | ---------------------------------- |
| Code execution       | Add a PythonToolAgent              |
| Web search           | Add a SearchToolAgent              |
| RAG / document QA    | Load embeddings + retriever        |
| Multi-step workflows | Add message history to both agents |

---

## ⚙️ Recommended Model Settings

| Model             | Use Case                            |
| ----------------- | ----------------------------------- |
| `claude-4-5-haiku`  | Fast + cheap everyday reasoning     |
| `claude-4-5-sonnet` | Better reasoning + writing          |
| `claude-4-1-opus`   | Deep reasoning, long context, plans |

---

## ⭐ Project Status

✅ Minimal agent collaboration
✅ Terminal chat UI
⏳ Optional: Code execution agent
⏳ Optional: RAG retrieval pipeline

---
