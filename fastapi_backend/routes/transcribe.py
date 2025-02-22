# fastapi_backend/routes/transcribe.py
from fastapi import APIRouter, UploadFile, File
from fastapi.responses import JSONResponse
import tempfile
import os
#from utils import load_whisper_model
from fastapi_backend.utils import load_whisper_model


router = APIRouter()
model = load_whisper_model()

@router.post("/transcribe/")
async def transcribe_audio(audio_file: UploadFile = File(...)):
    """Transcribes an audio file using Whisper."""
    try:
        # Save the uploaded file to a temporary location
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_audio:
            contents = await audio_file.read()
            temp_audio.write(contents)
            temp_file_path = temp_audio.name

        # Transcribe the audio file using Whisper
        result = model.transcribe(temp_file_path)
        transcription = result["text"]

        # Clean up the temporary file
        os.remove(temp_file_path)

        return JSONResponse({"transcription": transcription})

    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)