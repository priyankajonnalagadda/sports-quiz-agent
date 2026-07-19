import os
from pathlib import Path
from dotenv import load_dotenv

try:
    import streamlit as st
except ImportError:
    st = None

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# If running on Streamlit Cloud, read from Secrets
if not OPENAI_API_KEY and st is not None:
    try:
        OPENAI_API_KEY = st.secrets["OPENAI_API_KEY"]
    except Exception:
        pass

if not OPENAI_API_KEY:
    raise ValueError(
        "OPENAI_API_KEY not found. Add it to .env (local) or Streamlit Secrets (cloud)."
    )

CHROMA_DB_PATH = str(BASE_DIR / "chroma_db")
COLLECTION_NAME = "sports_history"

DEFAULT_MODEL = "tencent/hy3:free"

DEFAULT_RESULTS = 3