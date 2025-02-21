# streamlit_app/app.py
import streamlit as st
from audio_utils import record_audio
from model_utils import whisper_transcribe, summarize_long_text, extract_keywords #Model Utils now no longer loads model
from ui_elements import create_tabs, download_button
from utils import safe_delete_file
from langdetect import detect
from deep_translator import GoogleTranslator
import time
import requests
import tempfile #Add here

# Set Streamlit Page Config
st.set_page_config(page_title="Whisper Transcription & Analysis App", layout="wide")

st.title("🎙️ Whisper AI Transcription & Analysis App")


# Global Variables (Consider moving these to a config file)
RECORDING_DURATION = 25  # Set the recording duration to 25 seconds
BACKEND_URL = "http://127.0.0.1:8000" #Backend URL

# Create Tabs
tab1, tab2, tab3 = create_tabs()

# 🎤 Tab 1: Real-Time Recording
with tab1:
    st.header("🎤 Record Audio & Transcribe")

    if 'result' not in st.session_state:
        st.session_state['result'] = None  # Initialize the result
    if 'audio_path' not in st.session_state:
        st.session_state['audio_path'] = None  # Initialize the audio_path

    if st.button("Start Recording"):  # Use a single button
        recorded_file = record_audio(duration=RECORDING_DURATION)
        if recorded_file:  # Only proceed if recording was successful
            st.audio(recorded_file, format="audio/wav")
            st.success("✅ Recording Saved!")

            # Transcribe recorded audio
            try:
                result = whisper_transcribe(recorded_file)  #Just call it
                if result:
                    st.subheader("📝 Transcription:")
                    st.write(result["transcription"])
                    st.session_state['result'] = result  # Save result to session state for analysis
                    st.session_state['audio_path'] = recorded_file
                else:
                     st.error("Transcription failed.")

            except Exception as e:
                st.error(f"❌ Transcription error: {e}")

# 📁 Tab 2: File Upload
with tab2:
    st.header("📁 Upload Audio & Transcribe")
    audio_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

    if audio_file:
        if st.button("Transcribe Audio"):
            # Create a temporary file
            file_extension = audio_file.name.split(".")[-1]
            try:
                with tempfile.NamedTemporaryFile(delete=False, suffix=f".{file_extension}") as tmp_file:
                    tmp_file.write(audio_file.read())
                    file_path = tmp_file.name
                    tmp_file.close()  # Explicitly close the file

                    try:
                        result = whisper_transcribe(file_path) #Just call it
                        if result:
                            st.subheader("📝 Transcription:")
                            st.write(result["transcription"])
                            st.session_state['result'] = result  # Save result to session state for analysis
                            st.session_state['audio_path'] = file_path
                            # Language Detection and Translation
                            try:
                                detected_lang = detect(result["transcription"])
                                st.sidebar.info(f"🌍 Detected Language: {detected_lang}")

                                if detected_lang != "en":
                                    translated_text = GoogleTranslator(source=detected_lang, target="en").translate(
                                        result["transcription"])
                                    st.subheader("📜 Translated Text (English):")
                                    st.markdown(translated_text)
                            except Exception as e:
                                st.error(f"❌ Language detection/translation error: {e}")
                        else:
                             st.error("Transcription failed.")
                    except Exception as e:
                        st.error(f"❌ File processing/transcription error: {e}")

                    finally:
                        # Play audio *after* transcription
                        st.audio(audio_file)
                        time.sleep(0.05)  # Add a short delay, test different values
                        safe_delete_file(file_path)

            except Exception as e:
                st.error(f"❌ Error creating temporary file: {e}")

# 🔎 Tab 3: Analysis
with tab3:
    st.header("🔎 Analysis & Insights")

    if 'result' in st.session_state and 'audio_path' in st.session_state:
        result = st.session_state['result']
        audio_path = st.session_state['audio_path']

        # Button Alignment
        col1, col2 = st.columns(2)  # Create two columns

        with col1:  # Put Summarize button in the first column
            if st.button("Summarize"):
                try:
                    with st.spinner("Summarizing.."):
                        summary_text = summarize_long_text(result["transcription"]) #Now its the backend.
                        if summary_text:
                            st.subheader("📜 Summary:")
                            st.markdown(summary_text)
                        else:
                            st.warning(
                                "Summary could not be generated. The input text may be too short or contain invalid characters.")

                except Exception as e:
                    st.error(f"❌ Summarization error: {e}")

        with col2:  # Put Keywords button in the second column
            if st.button("Keywords"):
                try:
                    keywords = extract_keywords(result["transcription"]) #Now its the backend
                    if keywords:
                        st.subheader("🔑 Keywords:")
                        st.write(keywords)
                    else:
                         st.warning("Could not extract keywords. The input text may be too short or contain invalid characters.")

                except Exception as e:
                    st.error(f"❌ Keyword extraction error: {e}")

        st.markdown("Download All Results:")
        combined_text = "Transcription:\n"  # Initialize with a default value

        if result and isinstance(result, dict) and 'transcription' in result:
            combined_text += f"{result['transcription']}\n\n"
        else:
            combined_text += "No transcription available.\n\n"

        if 'summary_text' in locals() and summary_text:
            combined_text += f"Summary:\n{summary_text}\n\n"
        else:
            combined_text += "No summary available.\n\n"

        if 'keywords' in locals() and keywords:
            combined_text += f"Keywords:\n{', '.join(keywords)}\n\n"
        else:
            combined_text += "No keywords available.\n\n"

        download_html = download_button(combined_text, "analysis.txt", "Download as TXT")
        st.markdown(download_html, unsafe_allow_html=True)
    else:
        st.info("Transcribe audio first to enable analysis.")