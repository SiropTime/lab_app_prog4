import os

from dotenv import load_dotenv

load_dotenv(".env")

API_URL = os.environ.get("NYT_API_URL")
API_KEY = os.environ.get("NYT_API_KEY")
API_SECRET = os.environ.get("NYT_API_SECRET")
