import sys
import os

# Make the project root importable so we can pull in the Flask app
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app  # noqa: E402

# Vercel's Python runtime looks for a WSGI-compatible "app" object
