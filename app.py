import os
from flask import Flask, jsonify
import livekit

# Initialize Flask app
app = Flask(__name__)

# Load environment variables
LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_SECRET = os.getenv("LIVEKIT_SECRET")

# Validate environment variables
if not LIVEKIT_API_KEY or not LIVEKIT_SECRET:
    raise ValueError("LIVEKIT_API_KEY or LIVEKIT_SECRET is not set!")

@app.route("/")
def home():
    """
    Health check endpoint to verify the service is running.
    """
    return "LiveKit Restaurant Voice Agent is running!"

@app.route("/start-session")
def start_session():
    """
    Starts a LiveKit agent session.
    """
    try:
        # Initialize

