# IA no Terminal com Groq + Python 🐧⚡

Tutorial completo para rodar uma IA no terminal Linux usando a API da Groq.

---

# 1. Criar conta no Groq

Acesse:

https://console.groq.com

Faça login com Google, GitHub ou email.

---

# 2. Criar API Key

Entre em:

https://console.groq.com/keys

Clique em:

```text
Create API Key

A chave será algo como:

gsk_xxxxxxxxxxxxxxxxx

Guarde ela.
```
#3. Instalar dependências no Linux

Atualize o sistema:

sudo apt update

Instale o venv:

sudo apt install python3-venv
#4. Criar projeto
mkdir ~/ia-terminal
cd ~/ia-terminal
#5. Criar ambiente virtual
python3 -m venv venv

#6. Ativar ambiente virtual
source venv/bin/activate

Se funcionar aparecerá:

(venv)
#7. Instalar biblioteca Groq
pip install groq
#8. Criar arquivo da IA
nano ia.py
#9. Código da IA
from groq import Groq

print("Iniciando IA...")

client = Groq(
    api_key="SUA_CHAVE_GSK"
)

print("IA pronta!")

while True:
    pergunta = input(">>> ")

    resposta = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": pergunta
            }
        ],
        model="llama-3.3-70b-versatile"
    )

    print("\nIA:", resposta.choices[0].message.content)
#10. Colocar API Key

Troque:

SUA_CHAVE_GSK

pela sua chave real:

gsk_...
#11. Salvar no Nano
CTRL + O
ENTER
CTRL + X
#12. Executar IA
python3 ia.py
13. Resultado esperado
Iniciando IA...
IA pronta!
>>> oi
IA: Olá! Como posso ajudar?
#14. Rodar em outro terminal

Sempre execute:

cd ~/ia-terminal
source venv/bin/activate
python3 ia.py
#15. Transformar em comando global
Criar script
nano ~/ia

Cole:

#!/bin/bash

source ~/ia-terminal/venv/bin/activate
python3 ~/ia-terminal/ia.py
Dar permissão
chmod +x ~/ia
Mover para PATH
sudo mv ~/ia /usr/local/bin/ia
#16. Usar em qualquer terminal
ia
#17. Trocar modelos

Exemplo:

model="deepseek-r1-distill-llama-70b"

ou:

model="gemma2-9b-it"
Modelos disponíveis

https://console.groq.com/docs/models

Próximos upgrades
Memória
Voz
Execução de comandos Linux
Integração com Git
Automações
Copilot no terminal
IA offline com Ollama

