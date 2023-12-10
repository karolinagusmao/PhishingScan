import sys
import os
import pytest
import Flask

# Obtém o caminho para o diretório do backend (um nível acima do diretório do teste)
backend_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend'))

# Adiciona o caminho do backend ao sys.path
sys.path.append(backend_path)

# Importa a função verificar_phishing do arquivo app.py
from app import verificar_phishing

# Testes para verificar_phishing
@pytest.mark.parametrize("email_content, palavra_chave, esperado", [
    ("Este é um e-mail urgente que requer atenção imediata.", "urgente", True),
    ("Este é um e-mail normal, sem urgência.", "urgente", False),
    ("E-mail com a palavra-chave confidencial", "confidencial", True),
    ("Outro e-mail sem termos suspeitos", "confidencial", False),
])
def test_verificar_phishing(email_content, palavra_chave, esperado):
    resultado = verificar_phishing(email_content, palavra_chave)
    assert resultado == esperado
