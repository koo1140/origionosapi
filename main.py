from flask import Flask, request, jsonify
from gradio_client import Client

app = Flask(__name__)

@app.route('/qa')
def question():
    question_param = request.args.get('question') 
    print(question_param)

    client = Client("https://wop-originosai.hf.space/")
    result = client.predict(
				question_param,
				0.9,
				2048,
				0.9,
				1.2,
				api_name="/chat"
    )
    print(result)

    return jsonify({"question": question_param, "answer": result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
