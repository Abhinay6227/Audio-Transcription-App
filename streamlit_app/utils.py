# streamlit_app/utils.py
import os
import time
import streamlit as st
import base64
import tempfile #Add here

def safe_delete_file(filepath, retries=3, delay=1):
    """Attempts to delete a file with retries and error handling."""
    for i in range(retries):
        try:
            if os.path.exists(filepath):  # Check if the file exists before attempting to delete
                os.remove(filepath)
            return  # Success
        except PermissionError as e:
            if i < retries - 1:
                time.sleep(delay)
                continue  # Retry
            else:
                st.error(f"❌ PermissionError deleting {filepath}: {e}")  # Surface the error if all retries fail
                return  # Return without deleting
        except FileNotFoundError:
            # File no longer exists, so its "deleted"
            return
        except Exception as e:
            st.error(f"❌ Unexpected error deleting {filepath}: {e}")
            return  # Return without deleting
    return  # If it makes it here, something failed and we did not delete