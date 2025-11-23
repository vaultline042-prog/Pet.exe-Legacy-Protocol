from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

state = {"health": 100, "xp": 0, "mood": "Joyful", "tier": 1}

@app.route("/api/feed", methods=["POST"])
def feed():
    state["health"] = min(100, state["health"] + 10)
    state["xp"] += 1
    return jsonify({"ok": True, "state": state})

@app.route("/api/train", methods=["POST"])
def train():
    state["xp"] += 5
    return jsonify({"ok": True, "state": state})

@app.route("/api/play", methods=["POST"])
def play():
    state["mood"] = "Playful"
    state["xp"] += 2
    return jsonify({"ok": True, "state": state})

@app.route("/api/rest", methods=["POST"])
def rest():
    state["health"] = min(100, state["health"] + 5)
    state["mood"] = "Calm"
    return jsonify({"ok": True, "state": state})

@app.route("/api/reset", methods=["POST"])
def reset():
    state.update({"health": 100, "xp": 0, "mood": "Joyful", "tier": 1})
    return jsonify({"ok": True, "state": state})

@app.route("/api/stats", methods=["GET"])
def stats():
    return jsonify({"ok": True, "state": state})

@app.route("/api/logs", methods=["GET"])
def logs():
    return jsonify({"time": time.time(), "service": "pet-ex-backend", "status": "up"})

if __name__ == "__main__":
    app.run(debug=True)