📰 AI News Generator API
This is a FastAPI-based web service that provides:

✅ Real-time News fetched from NewsAPI

✅ AI-Generated News using Google's Gemini API

✅ Simple & fast REST API endpoints

✅ Built with FastAPI + Gemini + NewsAPI

📦 Features
Get real-time news about any topic

Generate AI-based news summaries

Built-in /docs (Swagger UI) for testing APIs

Easy to deploy on Railway / Render / Heroku

⚙️ Requirements
nginx
Copy
Edit
requests
fastapi
python-dotenv
google-generativeai
uvicorn
🛠️ Setup
Clone the repository

bash
Copy
Edit
git clone https://github.com/YOUR-USERNAME/ai-news-generator.git
cd ai-news-generator
Create & update .env

ini
Copy
Edit
NEWSAPI_KEY=your_newsapi_key
GEMINI_API_KEY=your_gemini_api_key
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 8000
🚀 API Endpoints
Method	Endpoint	Description
GET	/	Welcome Route
GET	/real-news?topic=technology	Get real-time news
GET	/ai-news?topic=technology	Get AI-generated news
📚 API Documentation
Once running, visit:
👉 http://localhost:8000/docs (Swagger UI)

🟣 Deployment Tip
Use this as your Start Command on Railway:

nginx
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port 8000
