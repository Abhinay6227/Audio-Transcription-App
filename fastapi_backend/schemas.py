# fastapi_backend/schemas.py
from pydantic import BaseModel

class TranscriptionResponse(BaseModel):
    transcription: str

class SummaryResponse(BaseModel):
    summary: str

class KeywordsResponse(BaseModel):
    keywords: list[str]