## AI News Generator API 📰

A FastAPI-based web service for generating AI-driven news content and fetching real-time news.

---

### ✅ Features
- Real-time news fetched from **NewsAPI**
- AI-generated news summaries using **Google's Gemini API**
- Simple & fast **REST API** endpoints
- Built with **FastAPI**, **Gemini**, and **NewsAPI**
- Interactive API docs using **Swagger UI**
- Ready for deployment on **Railway**, **Render**, or **Heroku**

---

### ⚙️ Tech Stack
- FastAPI
- REST API
- Google Generative AI (Gemini API)
- NewsAPI
- Uvicorn
- NGINX
- Python-dotenv
- Requests

---

### 📦 Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome Route |
| GET | `/real-news?topic=technology` | Get real-time news |
| GET | `/ai-news?topic=technology` | Get AI-generated news |

---

### 🟣 Setup Instructions

1. **Clone the Repository**

```bash
git clone https://github.com/YOUR-USERNAME/ai-news-generator.git
cd ai-news-generator
