from flask import Flask, render_template
import json, os

app = Flask(__name__)

DATA_PATH = os.path.join(os.path.dirname(__file__), "data", "resources.json")

def load_resources():
    with open(DATA_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

@app.route("/")
def home():
    resources = load_resources()
    return render_template("index.html", resources=resources)

if __name__ == "__main__":
    # Host 0.0.0.0 allows access from all network interfaces
    # port=5000 is the default; change if blocked
    app.run(debug=True, host="0.0.0.0", port=8000)
