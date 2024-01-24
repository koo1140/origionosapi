from flask import Flask, request, jsonify

app = Flask(name)

@app.route('/qa')
def question():
    question_param = request.args.get('question') 
    return jsonify({"question": question_param, "answer": "one lnol"})

if name == 'main':
    app.run(debug=True, host='0.0.0.0', port=5001)
