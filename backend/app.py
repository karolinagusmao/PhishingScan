from flask import Flask, jsonify, request

app = Flask(__name__)

def verificar_phishing(email_content, palavra_chave):
    if email_content.find(palavra_chave) != -1:
        return True
    return False

@app.route('/verificar-phishing', methods=['POST'])
def verificar_phishing_endpoint():
    data = request.json
    email_content = data.get('emailContent', '').lower()
    palavra_chave = data.get('palavraChave', '')
    encontrado = verificar_phishing(email_content, palavra_chave)
    return jsonify({'phishing': encontrado})

if __name__ == '__main__':
    app.run(debug=True)