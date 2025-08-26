from flask import Flask, jsonify
import main  # Importa last_signal do main.py

app = Flask(__name__)

@app.route('/signal', methods=['GET'])
def get_signal():
    """Retorna o último sinal"""
    return jsonify({"signal": main.last_signal if main.last_signal else "Aguardando..."})

if __name__ == "__main__":
    # Flask rodando na porta 8080 (obrigatório para Railway)
    app.run(host='0.0.0.0', port=8080)
