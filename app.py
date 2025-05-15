from flask import Flask
import livekit

app = Flask(__name__)

# Replace with your API key and secret
LIVEKIT_API_KEY = os.getenv ("APIKvHpGCMNMS9q")
LIVEKIT_SECRET = os.getenv("UNr52jrwItDtKtMb2Xf9t2n0K12ktkXiOD4zLlaCSXH")

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
