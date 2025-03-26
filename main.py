import os
import requests
from dotenv import load_dotenv
from fastapi import FastAPI
import google.generativeai as genai

# ✅ Load environment variables
load_dotenv()
NEWSAPI_KEY = os.getenv("NEWSAPI_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# ✅ Configure Gemini API
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro")  # Or any latest model

# ✅ Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to the AI & Real News API 🚀"}

# ✅ Fetch Real-Time News from NewsAPI
@app.get("/real-news")
def fetch_real_news(topic: str = "technology"):
    if not NEWSAPI_KEY:
        return {"status": "error", "message": "Missing NEWSAPI_KEY"}

    url = f"https://newsapi.org/v2/everything?q={topic}&apiKey={NEWSAPI_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])
        
        if articles:
            top_news = [{"title": a["title"], "url": a["url"]} for a in articles[:5]]  # Top 5 articles
            return {"status": "success", "topic": topic, "news": top_news}
        else:
            return {"status": "error", "message": "No news found"}
    else:
        return {"status": "error", "message": "Failed to fetch news"}

# ✅ Generate AI-Based News using Gemini AI
@app.get("/ai-news")
def generate_ai_news(topic: str = "latest technology news"):
    if not GEMINI_API_KEY:
        return {"status": "error", "message": "Missing GEMINI_API_KEY"}

    prompt = f"Summarize the latest news on {topic} in a neutral, journalistic style."

    try:
        response = model.generate_content(prompt)
        ai_generated_news = response.text
        return {"status": "success", "topic": topic, "ai_news": ai_generated_news}
    except Exception as e:
        return {"status": "error", "message": str(e)}

# ✅ Run FastAPI Server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
