from flask import Flask, request, jsonify
from flask_cors import CORS

import openai

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "http://127.0.0.1:5501/"}})


openai.api_key = "ENTER YOUR API KEY"


# get question response from open ai
def askGpt(question):

    response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question["question"]},
    ]
    )
    answer = {
        "prompt": question,
        "response": response.choices[0].message.content,
    }
    return answer


# connection to front end
@app.route('/askgpt', methods=['POST'])
def receive_json():
    if request.is_json:
        data = request.get_json()
        answer = askGpt(data)
        print(answer)
        return jsonify(answer)
    else:
        return "Request is not in JSON format"

if __name__ == '__main__':
    app.run(debug=True)