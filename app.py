from flask import Flask
app = Flask(__name__)

# Rota principal
@app.route("/")
def home():
    return "Robô de Day Trade rodando 🚀"

# Rota de teste de sinal (opcional)
@app.route("/signal")
def signal():
    return "Aqui vão os sinais CALL/PUT"

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 5000))  # Render define a porta
    app.run(host="0.0.0.0", port=port)
