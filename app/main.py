
from fastapi import FastAPI
from app.routers import analyzer

app = FastAPI(
    title="AI Text Automation API",
    description="Professional FastAPI backend for text summarization, keyword extraction and cleaning.",
    version="1.0.0"
)

app.include_router(analyzer.router, prefix="/analyze", tags=["Text Automation"])

@app.get("/")
def home():
    return {"status": "API is running", "message": "Welcome to AI Text Automation API"}
