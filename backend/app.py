from flask import Flask, request, jsonify
import openai
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Mengizinkan akses dari frontend

openai.api_key = "API_KEY_ANDA"

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": user_input}]
    )
    
    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(debug=True)
