import os
from flask import Flask

app = Flask(__name__)

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")
LIVEKIT_SECRET = os.getenv("LIVEKIT_SECRET")

if not LIVEKIT_API_KEY or not LIVEKIT_SECRET:
    print("LIVEKIT_API_KEY:", LIVEKIT_API_KEY)
    print("LIVEKIT_SECRET:", LIVEKIT_SECRET)
    raise ValueError("LIVEKIT_API_KEY or LIVEKIT_SECRET is not set!")

@app.route("/")
def home():
    return "LiveKit Restaurant Voice Agent is running!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
