from datetime import datetime
from flask import Flask, request, jsonify

app = Flask(__name__)


def get_time_based_greeting():
    """Return a greeting based on the time of day."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"


@app.route('/greet', methods=['GET'])
def greet():
    """Basic greeting endpoint."""
    name = request.args.get('name', 'World')
    return jsonify({
        "greeting": f"Hello, {name}!",
        "name": name
    })


@app.route('/greet/time', methods=['GET'])
def greet_by_time():
    """Time-based greeting endpoint."""
    name = request.args.get('name', 'World')
    time_greeting = get_time_based_greeting()
    return jsonify({
        "greeting": f"{time_greeting}, {name}!",
        "name": name,
        "time_of_day": time_greeting
    })


@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({"status": "healthy"})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
