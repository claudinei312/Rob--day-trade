from flask import Flask, render_template
import os

app = Flask(__name__)

# Rota principal
@app.route("/")
def home():
    return render_template("index.html")

# Rota para sinais do robô (exemplo)
@app.route("/signal")
def signal():
    return "CALL/PUT: sinal gerado aqui"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Render define a porta
    app.run(host="0.0.0.0", port=port)
