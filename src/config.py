import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY not found in .env file.")

CHROMA_DB_PATH = str(BASE_DIR / "chroma_db")
COLLECTION_NAME = "sports_history"

# Free OpenRouter model
DEFAULT_MODEL = "tencent/hy3:free"

DEFAULT_RESULTS = 3