# streamlit_app/ui_elements.py
import streamlit as st
import base64
import tempfile #Add here
def create_tabs():
    """Creates the main tabs for the Streamlit app."""
    tab1, tab2, tab3 = st.tabs(["🎤 Record", "📁 Upload & Transcribe", "🔎 Analysis"])
    return tab1, tab2, tab3


def download_button(object_to_download, download_filename, button_text):
    """Generates a link to download the given object_to_download."""
    if isinstance(object_to_download, bytes):
        pass
    else:
        try:
            object_to_download = object_to_download.encode().decode()
        except AttributeError:
            pass

    try:
        b64 = base64.b64encode(object_to_download.encode()).decode()
    except AttributeError:
        b64 = base64.b64encode(object_to_download).decode()

    button = f'<a href="data:file/txt;base64,{b64}" download="{download_filename}">{button_text}</a>'
    return button