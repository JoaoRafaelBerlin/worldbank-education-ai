import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)


def gerar_insight(indicador, tabela):

    prompt = f"""
Você é um especialista em educação mundial.

Analise o ranking abaixo.

Indicador:
{indicador}

Dados:
{tabela}

Explique:

- quais países lideram
- possíveis motivos
- tendências observadas
- recomendações para gestores públicos

Responda em português.
"""

    resposta = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )

    return resposta.choices[0].message.content