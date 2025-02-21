# Audio-Transcription-App

## Overview

This project is a web application that allows users to transcribe audio files into text using the Whisper ASR model. It consists of a FastAPI backend for handling transcription tasks and a Streamlit frontend for providing a user-friendly interface.

## Purpose

The primary use of this application is to provide a simple and accessible way to convert speech in audio files into written text. It can be used for various purposes, including:

*   **Transcription of Meetings and Lectures:** Convert recordings of meetings, lectures, and presentations into text for note-taking and documentation.
*   **Content Creation:** Quickly generate text transcripts for videos, podcasts, and other audio content, which can then be used for subtitles, captions, or blog posts.
*   **Accessibility:** Create transcripts for audio content to make it accessible to individuals with hearing impairments.
*   **Research and Analysis:** Transcribe audio data for qualitative research, linguistic analysis, and other data analysis tasks.

## Tech Stack

*   **Backend:**
    *   [FastAPI](https://fastapi.tiangolo.com/): A modern, high-performance web framework for building APIs with Python.
    *   [Whisper](https://github.com/openai/whisper): An Automatic Speech Recognition (ASR) system by OpenAI.
    *   [Uvicorn](https://www.uvicorn.org/): An ASGI server for running FastAPI applications.
    *   Python
*   **Frontend:**
    *   [Streamlit](https://streamlit.io/): An open-source Python library that makes it easy to build and share beautiful, custom web apps for machine learning and data science.

## Installation

Follow these steps to install and run the Audio Transcription App:

1.  **Clone the Repository:**

    ```bash
    git clone https://github.com/Abhinay6227/Audio-Transcription-App.git
    cd Audio-Transcription-App
    ```

2.  **Set up FastAPI Backend Virtual Environment:**

    ```bash
    cd fastapi_backend
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS and Linux
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

    *It is also recommended to downgrade NumPy due to conflicts with Numba, as whisper uses Numba.*

      ```bash
      pip uninstall numpy -y
      pip install numpy==2.1.6
      pip uninstall whisper -y
      pip install whisper
      ```

3.  **Set up Streamlit Frontend Virtual Environment:**

    Open a **new** terminal window.

    ```bash
    cd streamlit_app
    python -m venv venv
    venv\Scripts\activate  # On Windows
    # source venv/bin/activate  # On macOS and Linux
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```

## Running the Application

1.  **Start the FastAPI Backend:**

    In the terminal where you activated the backend environment, run:

    ```bash
    cd D:\...path to Audio-Transcription-App \Audio-Transcription-App\fastapi_backend
    uvicorn main:app --reload
    ```

    *   `main` is the name of your main Python file.
    *   `app` is the name of your FastAPI application instance.
    *   `--reload` enables automatic reloading of the server when you make changes.
    *   **Important:** Keep this terminal window running.

2.  **Start the Streamlit Frontend:**

    In the terminal where you activated the frontend environment, run:
     ```bash
        cd D:\...path to Audio-Transcription-App \Audio-Transcription-App\streamlit_app
     ```

    ```bash
    streamlit run app.py
    ```

    This will launch the Streamlit app in your web browser.

## Dependencies

The project relies on the following key dependencies:

**FastAPI Backend:**

*   `fastapi`: The core FastAPI framework.
*   `uvicorn`: An ASGI server for running FastAPI.
*   `whisper`: OpenAI's Whisper ASR library.
*   `python-multipart`: For handling file uploads with FastAPI.

**Streamlit Frontend:**

*   `streamlit`: For creating the user interface.
*   `requests`: For making HTTP requests to the backend API.

A complete list of dependencies, including specific versions, can be found in the `requirements.txt` files located in the `fastapi_backend` and `streamlit_app` directories.

## Configuration

*   **Backend URL:** The Streamlit frontend needs to know the URL of the FastAPI backend. This is typically configured in the `streamlit_app/app.py` (or related) file.  Ensure it is set to the correct address (usually `http://127.0.0.1:8000` or `http://localhost:8000`).

*   ## API Keys

This application relies on third-party services that require API keys, particularly OpenAI's Whisper ASR.  For security and proper functionality, you **must** provide your own API keys.

**Important:** This repository does *not* include any pre-configured API keys.  You are responsible for obtaining and securely managing your own keys.

**Obtaining API Keys:**

*   **OpenAI Whisper:** You will need an OpenAI API key to use the Whisper ASR functionality.  Visit the [OpenAI website](https://platform.openai.com/) to create an account and obtain your API key.

**Storing API Keys:**

It is **crucial** to store your API keys securely.  **Never** hardcode API keys directly in your code!  Instead, use one of the following methods:

*   **Environment Variables:**  The recommended approach is to store API keys as environment variables.  You can set environment variables on your system or use a `.env` file (see below).

*   **.env Files:** Create a `.env` file in the root directory of the project (or in the appropriate subdirectory, such as `fastapi_backend`).  Add your API keys to the `.env` file in the following format:

    ```
    OPENAI_API_KEY=YOUR_OPENAI_API_KEY
    ```

    **Important:**  Make sure to add `.env` to your `.gitignore` file to prevent your API keys from being committed to your repository!

*   **Secure Configuration Files:** For more complex deployments, consider using secure configuration management tools or services.

*Accessing API Keys in the Code:**

In your Python code, you can access environment variables using the `os` module:

```python
import os

openai_api_key = os.environ.get("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

# Now you can use the openai_api_key in your code

## Usage

1.  Open the Streamlit app in your web browser.
2.  Upload an audio file in a supported format (e.g., MP3, WAV).
3.  Click the "Transcribe" button.
4.  The app will send the audio file to the FastAPI backend for transcription.
5.  The transcribed text will be displayed in the Streamlit app.

## Troubleshooting

*   **`ImportError`:** If you get an `ImportError`, it means a package is missing. Activate the correct virtual environment and run `pip install <package_name>`.
*   **Connection Refused:** If the frontend cannot connect to the backend, ensure that:
    *   The backend is running *before* the frontend.
    *   The backend URL in the frontend is correct.
    *   The backend server is serving content at that URL.
*   **Numba/NumPy Error:** If you get an error related to Numba and NumPy versions, follow the NumPy downgrading instructions above.


## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues to report bugs or suggest new features.


