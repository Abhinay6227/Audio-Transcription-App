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




