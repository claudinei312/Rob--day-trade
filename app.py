from flask import Flask, render_template
import os

app = Flask(__name__)

# Rota principal - serve o index.html
@app.route("/")
def home():
    return render_template("index.html")

# Rota de sinais do robô
@app.route("/signal")
def signal():
    # Aqui você integra o seu robô real para gerar CALL/PUT
    return "Sinal atual: CALL"

if __name__ == "__main__":
    # Render exige que o app use a porta definida em PORT
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
