from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

# Replace with your OpenAI API key
client = OpenAI(api_key="YOUR_API_KEY_HERE")

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/settings")
def settings():
    return render_template("settings.html")

@app.route("/get_response", methods=["POST"])
def get_response():
    user_message = request.json.get("message")
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_message}]
        )
        bot_reply = response.choices[0].message.content
    except Exception as e:
        bot_reply = f"Error: {str(e)}"
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
