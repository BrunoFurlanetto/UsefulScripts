import os
from dotenv import load_dotenv


def load_env():
    """Load and validate environment variables from .env"""
    load_dotenv()

    config = {
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASS": os.getenv("DB_PASS"),
        "DB_HOST": os.getenv("DB_HOST", "localhost"),
        "DB_PORT": int(os.getenv("DB_PORT", 5432)),
        "DB_PREFIX": os.getenv("DB_PREFIX", ""),
        "MAIN_BRANCH": os.getenv("MAIN_BRANCH", "main"),
    }

    missing = [k for k, v in config.items() if not v]

    if missing:
        raise ValueError(f"Missing variables in .env: {', '.join(missing)}")

    return config
