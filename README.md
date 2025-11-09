
# 🤖 ClaudeAutoAgent — Web UI + Docker + SSL (Production + CI/CD + Render Deployment)

A **collaborative AI agent system** using **Microsoft AutoGen** and **Anthropic Claude**, served via a **FastAPI backend** and **Streamlit UI**, now fully deployed with:

- ✅ **GitHub Actions CI/CD**
- ✅ **Render cloud deployment**
- ✅ **Docker production build**

---

## ✨ Features

- 🧠 Two-Agent Cooperative Reasoning (Supervisor + Worker)
- 🌐 Streamlit Web UI
- ⚡ FastAPI Backend API
- 🐳 Dockerized (Production)
- 🔄 CI/CD using GitHub Actions (auto build + deploy)
- ☁️ Render Deployment Support (via `render.yaml`)

---

## 📁 Project Structure (Updated)

```

ClaudeAutoAgent/
│
├── agents.py
├── chat.py
├── main.py               # FastAPI API
├── app.py                # Streamlit UI
│
├── requirements.txt
├── .env
│
├── Dockerfile
├── docker-compose.yml
│
├── render.yaml           # Render deployment config
│
├── .github/
│   └── workflows/
│       └── deploy.yml    # GitHub Actions CI/CD pipeline
│
└── nginx/
├── nginx.conf
└── ssl/
├── server.crt
└── server.key

```

---

## 🔐 Environment Variables

Create `.env`:

```

ANTHROPIC_API_KEY=your_real_claude_key_here

````

---

## 🚀 Docker Run (Local Development / Testing)

```bash
docker compose up --build -d
````

Then visit:

```
http://localhost:8501  → Streamlit UI
http://localhost:8000  → FastAPI API Docs
```

---

## 🔄 CI/CD — GitHub Actions (deploy.yml)

```
.github/workflows/deploy.yml
```

The workflow:

* Triggers on `git push` to `main`
* Builds Docker image
* Deploys to Render

*No manual deployment needed.*

---

## ☁️ Deployment — Render

The deployment is controlled by:

```
render.yaml
```

This file:

* Defines **Web Service**
* Sets **runtime = Docker**
* Injects **environment variables**
* Exposes correct **PORT**

Once linked with GitHub → Render auto redeploys on push ✅

---

## 🌍 Access After Deployment

```
https://<your-service-name>.onrender.com/
```

If backend and UI are combined:

* Opening the URL loads Streamlit UI
* API available under `/api/...`

---

## ✅ Status

| Component         | State                 |
| ----------------- | --------------------- |
| Agents            | ✅ Working             |
| Streamlit UI      | ✅ Working             |
| FastAPI Backend   | ✅ Working             |
| Docker Build      | ✅ Working             |
| CI/CD Pipeline    | ✅ Auto Deploy Working |
| Render Deployment | ✅ Live                |

---


