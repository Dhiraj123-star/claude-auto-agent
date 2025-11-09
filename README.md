
# 🤖 ClaudeAutoAgent — Web UI + Docker + SSL (Production Edition)

A **collaborative AI agent system** using **Microsoft AutoGen** and **Anthropic Claude**, served via a **FastAPI backend**, a **Streamlit UI**, and **NGINX reverse proxy with SSL** — fully packaged in **Docker**.

This system uses a **Supervisor → Worker** collaboration pattern, where agents work together to produce better answers.

---

## ✨ Features

* 🧠 Two-Agent Collaborative Reasoning (Supervisor + Worker)
* 🌐 Streamlit Web Chat UI
* ⚡ FastAPI Backend API
* 🚀 Production runtime using **Gunicorn + Uvicorn workers**
* 🔒 HTTPS Support (Self-Signed or Real SSL Certificates)
* 🐳 Full **Docker & Docker Compose** deployment
* 🔄 NGINX reverse proxy (routes API + UI)

---

## 🛠️ Tech Stack

| Component           | Purpose                   |
| ------------------- | ------------------------- |
| **Python 3.12**     | Runtime                   |
| **FastAPI**         | Backend REST API          |
| **Streamlit**       | Web chat UI               |
| **Anthropic API**   | Claude model access       |
| **AutoGen**         | Multi-agent Orchestration |
| **Gunicorn**        | Production WSGI server    |
| **Uvicorn Workers** | Async backend runtime     |
| **NGINX**           | Reverse Proxy + SSL       |
| **Docker**          | Containerization          |

---

## 📁 Final Project Structure

```
ClaudeAutoAgent/
│
├── agents.py              # Defines Supervisor + Worker agents
├── chat.py                # Agent conversation orchestration
├── main.py                # FastAPI backend entrypoint
├── app.py                 # Streamlit UI
│
├── requirements.txt
├── .env                   # Stores ANTHROPIC_API_KEY
│
├── Dockerfile             # Multi-stage image build
├── docker-compose.yml     # Runs API + UI + NGINX reverse proxy
├── .dockerignore
│
└── nginx/
    ├── nginx.conf         # Reverse proxy config
    └── ssl/
        ├── server.crt     # SSL Certificate
        └── server.key     # SSL Private Key
```

---

## 🔐 Environment Variables

Create `.env`:

```
ANTHROPIC_API_KEY=your_real_claude_key_here
```

---

## 🐳 Running with Docker

### 1️⃣ Build + Start Everything

```bash
docker compose up --build -d
```

---

## 🌍 Access the Application

| Service      | URL                                                                |
| ------------ | ------------------------------------------------------------------ |
| **Frontend** | [https://localhost](https://localhost)                             |
| **Backend**  | [https://localhost/api/chat](https://localhost/api/chat) (proxied) |

> ✅ UI + API are now served securely via **NGINX over HTTPS**

---

## 🔧 Generate Self-Signed SSL Certificate (local testing)

```bash
mkdir -p nginx/ssl
openssl req -x509 -nodes -newkey rsa:2048 \
  -keyout nginx/ssl/server.key \
  -out nginx/ssl/server.crt \
  -days 365 \
  -subj "/CN=localhost"
```

Then restart:

```bash
docker compose restart nginx
```

---

## 🧠 Architecture Flow

```
User (Browser / Streamlit UI)
        ↓
      NGINX  (SSL termination + routing)
        ↓
   FastAPI Backend  ←→  Supervisor Agent
                        ↓
                    Worker Agent (Claude)
        ↓
  Response returned to UI
```

---

## 🧩 Extending the System

| Feature             | Modify                       |
| ------------------- | ---------------------------- |
| Add RAG / Knowledge | Inject retriever into Worker |
| Add tool calling    | Integrate PythonToolAgent    |
| Memory / history    | Persist messages in storage  |

---

## ✅ Status

| Feature                | Status    |
| ---------------------- | --------- |
| Two-Agent Reasoning    | ✅ Working |
| Streamlit UI           | ✅ Working |
| FastAPI Backend        | ✅ Working |
| Docker Production Mode | ✅ Working |
| SSL Reverse Proxy      | ✅ Working |

---
