from fastapi import FastAPI
from routes import transcribe, analyze  # Import
from utils import load_whisper_model  # Import the function
from fastapi.middleware.cors import CORSMiddleware  # Import CORS
import os
from fastapi_backend.routes import transcribe, analyze


# Initialize FastAPI app
app = FastAPI()

# CORS configuration (customize for production)
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ALLOWED_ORIGINS", "*").split(","),  # Change in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load API Key (Ensure it's set in Render environment settings)
API_KEY = os.getenv("API_KEY")
if not API_KEY:
    raise ValueError("⚠️ API_KEY not found! Set it in your environment variables.")

# Include the routers
app.include_router(transcribe.router)
app.include_router(analyze.router)

@app.get("/")
async def root():
    return {"message": "Whisper API is running"}

