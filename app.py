from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

# Load events
with open("data/events.json") as f:
    events = json.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    data = request.json
    query = data.get("query", "").lower()

    results = [e for e in events if query in e["name"].lower()]

    if results:
        return jsonify({"response": results})
    else:
        return jsonify({"response": [{"name": "No events found", "location": "", "date": ""}]})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)