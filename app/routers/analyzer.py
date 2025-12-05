from fastapi import APIRouter
from app.models.request_models import TextRequest
from app.utils.summarizer import generate_summary
from app.utils.keywords import extract_keywords
from app.utils.cleaner import remove_duplicate_lines, remove_duplicate_paragraphs

router = APIRouter()

@router.post("/")
def analyze(request: TextRequest):
    text = request.text

    summary = generate_summary(text)
    keywords = extract_keywords(text)
    clean_lines = remove_duplicate_lines(text)
    clean_paragraphs = remove_duplicate_paragraphs(text)

    response = {
        "summary": summary,
        "keywords": keywords,
        "clean_lines": clean_lines,
        "clean_paragraphs": clean_paragraphs
    }

    return {"status": "success", "analysis": response}
