# fastapi_backend/routes/analyze.py
from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import JSONResponse
from typing import Optional
from fastapi_backend.utils import load_summarization_pipeline, load_keybert_model

router = APIRouter()
summarizer = load_summarization_pipeline()
kw_model = load_keybert_model()

@router.get("/summarize/")
async def summarize_text(text: str = Query(..., title="Text to Summarize")):
    """Summarizes a given text."""
    if not summarizer:
        raise HTTPException(status_code=500, detail="Summarization model not loaded")
    try:
        summary = summarizer(text, max_length=130, min_length=30, do_sample=False)
        return JSONResponse({"summary": summary[0]['summary_text']})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/keywords/")
async def extract_keywords(text: str = Query(..., title="Text to Extract Keywords From"),
                            top_n: int = Query(5, title="Number of Keywords")):
    """Extracts keywords from a given text."""
    if not kw_model:
        raise HTTPException(status_code=500, detail="KeyBERT model not loaded")
    try:
        keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(1, 2), stop_words='english', top_n=top_n)
        return JSONResponse({"keywords": [kw[0] for kw in keywords]})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))