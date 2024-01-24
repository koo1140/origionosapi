from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/qa')
def question():
    question_param = request.args.get('question') 
    return f'The value of the "question" parameter is: {question_param}'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
