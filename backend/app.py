from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/verificar-phishing', methods=['POST'])
def verificar_phishing():
    data = request.json
    email_content = data.get('emailContent', '').lower()
    palavras_chave_phishing = ['urgente', 'confidencial', 'senha expirada', 'verificação de conta']
    encontrado = any(palavra in email_content for palavra in palavras_chave_phishing)
    return jsonify({'phishing': encontrado})

if __name__ == '__main__':
    app.run(debug=True)
