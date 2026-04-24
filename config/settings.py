import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

MODEL_NAME = "gpt-4o-mini"
EMBED_MODEL = "text-embedding-3-small"

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K = 4