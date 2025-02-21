# fastapi_backend/utils.py
import whisper
from transformers import pipeline
from keybert import KeyBERT
import os
from functools import lru_cache

@lru_cache(maxsize=1)
def load_whisper_model(model_name="base"):
    """Loads the Whisper ASR model."""
    try:
        model = whisper.load_model(model_name)
        print("✅ Whisper Model Loaded")
        return model
    except Exception as e:
        print(f"❌ Whisper Model Loading Error: {e}")
        return None

@lru_cache(maxsize=1)
def load_summarization_pipeline(model_name="sshleifer/distilbart-cnn-12-6"):
    """Loads the summarization pipeline."""
    try:
        summarizer = pipeline("summarization", model=model_name)
        print("✅ Summarization Pipeline Loaded")
        return summarizer
    except Exception as e:
        print(f"❌ Summarization pipeline not available (requires transformers).")
        return None

@lru_cache(maxsize=1)
def load_keybert_model():
    """Loads the KeyBERT model."""
    try:
        kw_model = KeyBERT()
        print("✅ KeyBERT Model Loaded")
        return kw_model
    except Exception as e:
        print(f"❌ Error loading KeyBERT")
        return None