import os
from flask import Flask, jsonify, send_from_directory
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
        # Initialize LiveKit session
        session = livekit.AgentSession(LIVEKIT_API_KEY, "room_name")
        session.start()
        return "Session started!"
    except Exception as e:
        # Log and return error details
        error_message = str(e)
        print(f"Error: {error_message}")
        return jsonify({"error": error_message}), 500

@app.route('/favicon.ico')
def favicon_ico():
    """
    Serves the favicon.ico from the .github directory.
    """
    return send_from_directory(
        os.path.join(app.root_path, '.github'),
        'banner_dark.png',
        mimetype='image/png'
    )

# Debug route to check environment variables (remove this in production)
@app.route("/debug-env")
def debug_env():
    """
    Returns the environment variables for debugging.
    """
    return {
        "LIVEKIT_API_KEY": LIVEKIT_API_KEY,
        "LIVEKIT_SECRET": LIVEKIT_SECRET
    }

if __name__ == "__main__":
    # Run the app
    app.run(host="0.0.0.0", port=5000)
