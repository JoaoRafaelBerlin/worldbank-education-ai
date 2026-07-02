import os
import pandas as pd
from dotenv import load_dotenv
from openai import OpenAI

# ==========================
# Carregar chave da API
# ==========================
load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

# ==========================
# Ler o dataset tratado
# ==========================
df = pd.read_csv("data/processed/education_clean.csv")

# Indicador que será analisado
indicador = "Adjusted net enrolment rate, primary, both sexes (%)"

# ==========================
# Gerar ranking
# ==========================
ranking = df[df["Indicator Name"] == indicador].copy()

ranking["Melhor Valor"] = ranking[
    ["2000", "2005", "2010", "2015"]
].max(axis=1)

ranking = ranking.dropna(subset=["Melhor Valor"])

ranking = ranking.sort_values(
    by="Melhor Valor",
    ascending=False
)

top10 = ranking[
    ["Country Name", "Melhor Valor"]
].head(10)

print("\nTOP 10 PAÍSES\n")
print(top10)

# ==========================
# Prompt para a IA
# ==========================
dados = top10.to_string(index=False)

prompt = f"""
Você é um especialista em educação global.

Analise o ranking abaixo.

Explique:

1. Quais países apresentam melhor desempenho.
2. Quais padrões podem ser observados.
3. Possíveis explicações para esses resultados.
4. Recomendações para países com desempenho inferior.

Ranking:

{dados}
"""

print("\nEnviando para o Groq...\n")

# ==========================
# Chamada da IA
# ==========================
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

texto = resposta.choices[0].message.content

# Mostrar resposta
print(texto)

# ==========================
# Salvar relatório
# ==========================
os.makedirs("reports", exist_ok=True)

with open(
    "reports/education_report.txt",
    "w",
    encoding="utf-8"
) as arquivo:

    arquivo.write(texto)

print("\nRelatório salvo em reports/education_report.txt")