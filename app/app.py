# A simple Flask web app — the pipeline is what matters, not the app itself
from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Cloud Infrastructure Pipeline is running",
        "author":  "Atefor Lesley Nkezi",
        "status":  "healthy"
    })

@app.route('/health')
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)