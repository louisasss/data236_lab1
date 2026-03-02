# Data 236 Lab 1 - Yelp

A Yelp-style restaurant discovery and review platform built with **React + Vite + TailwindCSS** (frontend) and **FastAPI + MySQL** (backend), with an **AI Assistant** powered by LangChain and Tavily.

---

## Project Structure

```
/
├── frontend/    # React + Vite + TailwindCSS
└── backend/     # FastAPI + SQLAlchemy + MySQL
```

---

## Prerequisites

- Node.js >= 18
- Python >= 3.11
- MySQL >= 8.0
- OpenAI API key (for AI assistant)
- Tavily API key (for AI web search)

---

## Backend Setup

```bash
cd backend

# 1. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate        # Mac/Linux
# venv\Scripts\activate         # Windows

# 2. Install dependencies
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env with your MySQL credentials, JWT secret, and API keys

# 4. Create the MySQL database
mysql -u root -p -e "CREATE DATABASE yelpclone CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"

# 5. Create all tables
python init_db.py

# 6. Start the dev server
uvicorn app.main:app --reload --port 8000
```

API docs available at: http://localhost:8000/docs

---

## Frontend Setup

```bash
cd frontend

# 1. Install dependencies
npm install

# 2. Configure environment (optional)
cp .env.example .env

# 3. Start the dev server
npm run dev
```

App runs at: http://localhost:5173

---

## API Keys

| Key | Where to get it |
|---|---|
| `OPENAI_API_KEY` | https://platform.openai.com/api-keys |
| `TAVILY_API_KEY` | https://app.tavily.com |

---

## Development Workflow

1. Backend runs on port **8000** — Vite proxies `/api` requests to it automatically.
2. Never commit `.env` files — each developer copies `.env.example` and fills in their own values.
3. After pulling changes that add new models, re-run `python init_db.py` (or handle with migrations).

---

## Contributors

- Muhammad Faiq Salman
- Louisa Stumpf
