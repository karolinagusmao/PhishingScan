function verificarPhishing() {
    console.log('Botão de verificação clicado!'); // Verificação de clique no botão (verifique no console do navegador)
  
    const emailContent = document.getElementById('emailContent').value;
  
    fetch('/verificar-phishing', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ emailContent })
    })
    .then(response => response.json())
    .then(data => {
      const resultElement = document.getElementById('result');
      if (data.phishing) {
        resultElement.innerText = 'Este e-mail parece ser um possível phishing.';
        resultElement.style.color = 'red';
      } else {
        resultElement.innerText = 'Este e-mail parece ser legítimo.';
        resultElement.style.color = 'green';
      }
    })
    .catch(error => console.error('Erro:', error));
  }
  