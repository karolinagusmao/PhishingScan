import sys
import os
import pytest

# Obtém o caminho para o diretório do backend (um nível acima do diretório do teste)
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend'))

# Adiciona o caminho do backend ao sys.path
sys.path.append(backend_path)

# Importa a função verificar_phishing do arquivo app.py
from app import verificar_phishing

# Testes
def test_verificar_phishing_encontra_palavra_chave():
    email_content = "Este é um e-mail urgente que requer atenção imediata."
    palavra_chave = "urgente"

    resultado = verificar_phishing(email_content, palavra_chave)

    assert resultado == True  # Esperamos que a palavra-chave "urgente" seja encontrada no e-mail

def test_verificar_phishing_nao_encontra_palavra_chave():
    email_content = "Este é um e-mail normal, sem urgência."
    palavra_chave = "urgente"

    resultado = verificar_phishing(email_content, palavra_chave)

    assert resultado == False  # Não esperamos que a palavra-chave "urgente" seja encontrada no e-mail
