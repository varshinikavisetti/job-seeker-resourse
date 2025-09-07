from flask import Flask, render_template
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'

# Load resources
resources = {}
resource_path = os.path.join("data", "resources.json")
if os.path.exists(resource_path):
    with open(resource_path) as f:
        resources = json.load(f)
else:
    print("⚠️ resources.json not found!")

# Home route
@app.route('/')
def home():
    return render_template("index.html", resources=resources)

if __name__ == "__main__":
    app.run(debug=True)
