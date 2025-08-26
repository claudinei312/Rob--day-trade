from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "Robô de Day Trade rodando no Render 🚀"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render define a porta
    app.run(host="0.0.0.0", port=port)
