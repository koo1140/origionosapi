from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return "test"

@app.route('/ai', methods=['GET'])
def AI_endpoint():
    response = "hi"
    return jsonify({'response': response})

def start():
    app.run(debug=True, port=5000, host='0.0.0.0')
