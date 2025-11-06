Got it — we must **update the README to match the latest architecture**, which now includes:

* **FastAPI backend (main.py)**
* **Agents defined in agents.py**
* **Chat orchestration in chat.py**
* **Streamlit UI (app.py)** instead of TUI

Here is the **fully updated README**, clean and complete:

---

# 🤖 ClaudeAutoAgent — Web UI (Streamlit Edition)

A **collaborative AI agent system** powered by **Microsoft AutoGen** and **Anthropic Claude**, now with a **modern Streamlit web interface**.

This version uses a **Supervisor → Worker agent collaboration** and provides a **simple chat interface** in the browser.

---

## ✨ Features

* 🌐 **Web-based UI** built using **Streamlit**
* 🧠 **Two-Agent Collaboration**

  * **Supervisor Agent** → interprets tasks
  * **Worker Agent** → reasons + generates final answer
* 🔄 **FastAPI backend** to run structured agent communication
* 🔐 Uses **Claude (Anthropic API)** models
* 🧱 Clean architecture, simple to extend

---

## 🛠️ Tech Stack

| Component         | Purpose                      |
| ----------------- | ---------------------------- |
| **Python 3.10+**  | Runtime environment          |
| **autogen**       | Multi-agent orchestration    |
| **anthropic API** | Claude model access          |
| **FastAPI**       | Backend web service          |
| **Streamlit**     | Web UI                       |
| **python-dotenv** | Environment variable loading |

---

## 📁 Project Structure

```
ClaudeAutoAgent/
│
├── agents.py       # Defines worker & supervisor agents
├── chat.py         # Handles agent-to-agent conversation logic
├── main.py         # FastAPI backend server
├── app.py          # Streamlit UI
├── .env            # Stores ANTHROPIC_API_KEY
└── requirements.txt
```

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
source venv/bin/activate      # Mac / Linux
venv\Scripts\activate         # Windows
```

### 3️⃣ Install Dependencies

```bash
uv pip install -r requirements.txt
```

### 4️⃣ Add Your Claude API Key

Create a `.env` file:

```
ANTHROPIC_API_KEY=your_real_key_here
```

---

## 🚀 Running the Application

### Start Backend (FastAPI)

```bash
uvicorn main:app --reload
```

Runs at:

```
http://127.0.0.1:8000
```

### Start Frontend (Streamlit UI)

```bash
streamlit run app.py
```

Runs at:

```
http://localhost:8501
```

---

## 🧠 How It Works

```
User (Streamlit UI)
      ↓
   FastAPI
      ↓
Supervisor Agent  → interprets request
      ↓
Worker Agent      → generates detailed response
      ↓
Response returned to UI and displayed
```

---

## 🧩 Extending the System

| Feature to Add      | Code to Modify                     |
| ------------------- | ---------------------------------- |
| Code execution      | Add PythonToolAgent in `agents.py` |
| Web search          | Integrate search tool agent        |
| RAG / document QA   | Load embeddings + retriever        |
| Multi-step planning | Maintain conversation history      |

---

## ⭐ Project Status

✅ Working Agent Collaboration
✅ Streamlit Chat UI
✅ FastAPI Integration
⏳ Optional: Persistent chat history
⏳ Optional: Tool-enabled worker agent

---

