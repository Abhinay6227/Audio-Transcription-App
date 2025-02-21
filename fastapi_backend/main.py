# fastapi_backend/main.py
from fastapi import FastAPI
from routes import transcribe, analyze #Import
from utils import load_whisper_model  # Import the function
from fastapi.middleware.cors import CORSMiddleware #Import CORS
import os

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins in development (configure this in production)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(transcribe.router)
app.include_router(analyze.router)

@app.get("/")
async def root():
    return {"message": "Whisper API is running"}