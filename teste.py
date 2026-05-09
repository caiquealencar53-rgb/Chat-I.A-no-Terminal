from groq import Groq

print("Iniciando IA...")

client = Groq(
    api_key="KEY_API"
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
