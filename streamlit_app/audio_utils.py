# streamlit_app/audio_utils.py
import streamlit as st
import sounddevice as sd
import numpy as np
import scipy.io.wavfile as wav
import tempfile #Add here

def record_audio(duration=5, samplerate=44100):
    """Records audio from the microphone for a specified duration."""
    st.sidebar.info(f"🎤 Recording for {duration} seconds...")
    try:
        audio_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype=np.int16)
        sd.wait()
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp_file:
            file_path = tmp_file.name
            wav.write(file_path, samplerate, audio_data)
        return file_path
    except Exception as e:
        st.error(
            f"❌ Audio recording error: {e}.  Make sure you have a microphone connected and sounddevice is configured correctly.")
        return None