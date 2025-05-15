from flask import Flask
import livekit

app = Flask(__name__)

# Replace with your API key and secret
LIVEKIT_API_KEY = "your_api_key"
LIVEKIT_SECRET = "your_secret"

@app.route("/")
def home():
    return "LiveKit Restaurant Voice Agent is running!"

@app.route("/start-session")
def start_session():
    session = livekit.AgentSession(LIVEKIT_API_KEY, "room_name")
    session.start()
    return "Session started!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
