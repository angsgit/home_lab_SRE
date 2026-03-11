from flask import Flask, jsonify
import time
import random

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(message="Hello from your SRE lab!")

@app.route("/work")
def work():
    # simulate some processing delay
    delay = random.uniform(0, 2)  # 0–2 seconds
    time.sleep(delay)
    return jsonify(status="done", delay=delay)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)