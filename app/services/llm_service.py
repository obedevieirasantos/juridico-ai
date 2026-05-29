import os

from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def gerar_resposta(contexto, pergunta):
    prompt = f"""
    Voce e um assistente juridico especializado em analise de contratos.

    Responda apenas com base no contexto abaixo. Se o contexto nao for suficiente,
    diga que nao encontrou informacoes suficientes no documento.

    Estruture a resposta com:
    - resposta direta;
    - principais riscos ou pontos relevantes;
    - observacao de que a analise nao substitui revisao de um advogado.

    Contexto:
    {contexto}

    Pergunta:
    {pergunta}
    """

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    resposta = chat_completion.choices[0].message.content

    return resposta
