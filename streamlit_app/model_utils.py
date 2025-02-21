# streamlit_app/model_utils.py
import streamlit as st
import requests
import base64 #Base 64
import tempfile #Add here
BACKEND_URL = "http://127.0.0.1:8000"

def whisper_transcribe(audio_path): #Removed model
    """Transcribes an audio file using the backend API."""
    try:
        with open(audio_path, 'rb') as audio_file:
            files = {'audio_file': audio_file}
            with st.spinner("Transcribing via Backend..."):
                response = requests.post(f"{BACKEND_URL}/transcribe/", files=files)
            response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
            result = response.json()
            if "transcription" in result:
                return result #Only return the whole JSON result
            else:
                st.error(f"❌ Transcription failed on backend: {result.get('detail', 'Unknown error')}")
                return None
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error connecting to transcription backend: {e}")
        return None


def summarize_long_text(text, max_length=130, min_length=30):#Removed Summarizer since it runs on backend
    """Summarizes a long text using the backend API."""
    try:
        params = {"text": text}
        response = requests.get(f"{BACKEND_URL}/summarize/", params=params)
        response.raise_for_status()
        summary_result = response.json()
        return summary_result.get("summary") #Just get the summary
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error connecting to summarization backend: {e}")
        return None

def extract_keywords(text, top_n=5): #Removed KeyModel since it runs on backend
    """Extracts keywords from a given text using the backend API."""
    try:
        params = {"text": text, "top_n": top_n}
        response = requests.get(f"{BACKEND_URL}/keywords/", params=params)
        response.raise_for_status()
        keywords_result = response.json()
        return keywords_result.get("keywords") #Just get the keywords
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Error connecting to keyword extraction backend: {e}")
        return None