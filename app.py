from flask import Flask, jsonify, render_template, request

from ai_assistant import AiCoder

app = Flask(__name__)
assistant = AiCoder()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/chat", methods=["POST"])
def chat():
    payload = request.get_json(silent=True) or {}
    message = payload.get("message", "").strip()

    if not message:
        return jsonify({"reply": "Please enter a message before sending."}), 400

    reply = assistant.chat(message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
