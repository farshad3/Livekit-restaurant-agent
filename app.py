from flask import Flask, jsonify
import livekit
import os

app = Flask(__name__)

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY", None)
LIVEKIT_SECRET = os.getenv("LIVEKIT_SECRET", None)

if not LIVEKIT_API_KEY or not LIVEKIT_SECRET:
    raise ValueError("LIVEKIT_API_KEY or LIVEKIT_SECRET is not set!")

@app.route("/")
def home():
    return "LiveKit Restaurant Voice Agent is running!"

@app.route("/start-session")
def start_session():
    try:
        session = livekit.AgentSession(LIVEKIT_API_KEY, "room_name")
        session.start()
        return "Session started!"
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
