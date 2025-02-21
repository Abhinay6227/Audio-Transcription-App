# Audio Transcription App

## Overview

This project is a web application that allows users to transcribe audio files into text using the Whisper ASR model. It consists of a FastAPI backend for handling transcription tasks and a Streamlit frontend for providing a user-friendly interface. This document provides comprehensive instructions for setting up, running, and using the application.

## Purpose

The primary use of this application is to provide a simple and accessible way to convert speech in audio files into written text. It can be used for various purposes, including:

*   **Transcription of Meetings and Lectures:** Convert recordings of meetings, lectures, and presentations into text for note-taking and documentation.
*   **Content Creation:** Quickly generate text transcripts for videos, podcasts, and other audio content, which can then be used for subtitles, captions, or blog posts.
*   **Accessibility:** Create transcripts for audio content to make it accessible to individuals with hearing impairments.
*   **Research and Analysis:** Transcribe audio data for qualitative research, linguistic analysis, and other data analysis tasks.

## Tech Stack

The application is built using the following technologies:

*   **Backend (fastapi_backend directory):**
    *   [FastAPI](https://fastapi.tiangolo.com/): A modern, high-performance web framework for building APIs with Python.
    *   [Whisper](https://github.com/openai/whisper): An Automatic Speech Recognition (ASR) system by OpenAI.
    *   [Uvicorn](https://www.uvicorn.org/): An ASGI server for running FastAPI applications.
    *   `python-multipart`: Used for handling file uploads in the backend.
    *   Python
*   **Frontend (streamlit_app directory):**
    *   [Streamlit](https://streamlit.io/): An open-source Python library that makes it easy to build and share custom web apps for machine learning and data science.
    *   `requests`: Used for making HTTP requests from the frontend to the backend API.
    *   Python

## Installation and Setup (Windows)

These instructions are for setting up the application on a Windows system.

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Abhinay6227/Audio-Transcription-App.git
    cd Audio-Transcription-App
    ```

2.  **Set up FastAPI Backend Virtual Environment:**

    ```bash
    cd fastapi_backend
    python -m venv venv
    venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    **Important: NumPy and Numba Compatibility**

    The Whisper library relies on `numba`, which may have compatibility issues with newer versions of `numpy`. If you encounter errors related to `numba` or `numpy`, try downgrading `numpy` as follows:

    ```bash
    pip uninstall numpy -y
    pip install numpy==2.1.6
    pip uninstall whisper -y
    pip install whisper
    ```

3.  **Set up Streamlit Frontend Virtual Environment:**

    Open a **new** terminal window!  It is crucial to use a separate terminal for the frontend.

    ```bash
    cd D:\...your path to Audio-Transcription-App \Audio-Transcription-App\streamlit_app
    python -m venv venv
    venv\Scripts\activate
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

## API Keys

This application requires an OpenAI API key to use the Whisper ASR functionality in the backend.

**Important:** This repository does *not* include any pre-configured API keys. You are responsible for obtaining and securely managing your own key.

**Obtaining an OpenAI API Key:**

*   Visit the [OpenAI website](https://platform.openai.com/) to create an account and obtain your API key.

**Storing the API Key:**

It is **crucial** to store your API key securely. **Never** hardcode it directly in your code! The recommended approach is to use environment variables.

*   **.env File:** Create a `.env` file in the `fastapi_backend` directory. Add your API key to the `.env` file:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

    **Important:** Add `.env` to your `.gitignore` file to prevent your API key from being committed to your repository!

**Accessing the API Key in the Code (Backend):**

In the `fastapi_backend` code, access the API key using the `os` module:

```python
import os

openai_api_key = os.environ.get("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Now you can use the openai_api_key in your code
content_copydownload
Use code with caution.
Markdown
Configuration
Backend URL (Frontend): The Streamlit frontend needs to know the URL of the FastAPI backend. Open the streamlit_app/app.py file (or any relevant utility files). Locate the line that defines the backend URL (e.g., BACKEND_URL = "http://127.0.0.1:8000/transcribe"). Ensure it is set to the correct address where your FastAPI backend will be running (typically http://127.0.0.1:8000).

Running the Application (Windows)
Start the FastAPI Backend:

Open a command prompt or PowerShell window.

Navigate to the backend directory:

cd D:\...your path to Audio-Transcription-App \Audio-Transcription-App\fastapi_backend
content_copydownload
Use code with caution.
Bash
Activate the backend virtual environment:

venv\Scripts\activate
content_copydownload
Use code with caution.
Bash
Run the FastAPI application:

uvicorn main:app --reload
content_copydownload
Use code with caution.
Bash
Keep this terminal window running.

Start the Streamlit Frontend:

Open a new command prompt or PowerShell window.

Navigate to the frontend directory:

cd D:\...your path to Audio-Transcription-App \Audio-Transcription-App\streamlit_app
content_copydownload
Use code with caution.
Bash
Activate the frontend virtual environment:

venv\Scripts\activate
content_copydownload
Use code with caution.
Bash
Run the Streamlit application:

streamlit run app.py
content_copydownload
Use code with caution.
Bash
This will launch the Streamlit app in your web browser.

Dependencies
The project relies on the following key dependencies:

FastAPI Backend:

fastapi

uvicorn

whisper

python-multipart

Streamlit Frontend:

streamlit

requests

A complete list of dependencies, including specific versions, can be found in the requirements.txt files located in the fastapi_backend and streamlit_app directories.

Usage
Open the Streamlit app in your web browser.

Upload an audio file in a supported format (e.g., MP3, WAV).

Click the "Transcribe" button.

The app will send the audio file to the FastAPI backend for transcription.

The transcribed text will be displayed in the Streamlit app.

Troubleshooting
ImportError: If you get an ImportError, it means a package is missing. Activate the correct virtual environment (either the backend or frontend environment, depending on where the error occurs) and run pip install <package_name>.

Connection Refused: If the frontend cannot connect to the backend, ensure that:

The backend server is running before you start the frontend.

The backend URL in the frontend code is correct.

The backend server is actually serving content at that URL. You can test this by opening the URL in a web browser (e.g., http://127.0.0.1:8000/ or http://localhost:8000/). You should see a FastAPI welcome message or API documentation.

Numba/NumPy Error: If you get an error related to Numba and NumPy versions in the fastapi_backend, follow the NumPy downgrading instructions in the Installation section.

Contributing
Contributions are welcome! Please feel free to submit pull requests or open issues to report bugs or suggest new features.

