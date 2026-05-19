from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def gerar_resposta(contexto, pergunta):

    prompt = f"""
    Você é um assistente jurídico.

    Responda apenas com base no contexto abaixo.

    Contexto:
    {contexto}

    Pergunta:
    {pergunta}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        model="llama-3.3-70b-versatile"
    )

    resposta = chat_completion.choices[0].message.content

    return resposta