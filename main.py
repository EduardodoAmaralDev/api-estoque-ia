from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/prever', methods=['POST'])
def prever():
    try:
        dados = request.json
        
        df = pd.DataFrame(dados)

        # previsão simples (média)
        media = df['total_vendido'].mean()
        previsao = round(media * 30)

        return jsonify({
            "status": "ok",
            "previsao_proximo_mes": previsao
        })

    except Exception as e:
        return jsonify({
            "status": "erro",
            "mensagem": str(e)
        })

@app.route('/')
def home():
    return "API de previsão funcionando!"

import os

port = int(os.environ.get("PORT", 5000))
app.run(host='0.0.0.0', port=port)