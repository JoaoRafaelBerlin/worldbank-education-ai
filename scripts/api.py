from fastapi import FastAPI
import pandas as pd
from scripts.ai import gerar_insight

app = FastAPI()

df = pd.read_csv("data/processed/education_clean.csv")


@app.get("/")
def home():
    return {
        "status": "ok",
        "projeto": "World Bank Education AI"
    }


@app.get("/ranking")
def ranking(indicador: str):

    ranking = df[
        df["Indicator Name"] == indicador
    ].copy()

    ranking["Melhor Valor"] = ranking[
        ["2000", "2005", "2010", "2015"]
    ].max(axis=1)

    ranking = ranking.dropna(subset=["Melhor Valor"])

    ranking = ranking.sort_values(
        by="Melhor Valor",
        ascending=False
    )

    return ranking[
        ["Country Name", "Melhor Valor"]
    ].head(10).to_dict(orient="records")


@app.get("/compare")
def compare(
    country1: str,
    country2: str,
    indicator: str
):

    dados = df[
        (df["Country Name"].isin([country1, country2])) &
        (df["Indicator Name"] == indicator)
    ]

    if dados.empty:
        return {"erro": "Nenhum dado encontrado"}

    return dados.to_dict(orient="records")


@app.get("/insights")
def insights(indicador: str):

    ranking = df[
        df["Indicator Name"] == indicador
    ].copy()

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

    texto = top10.to_string(index=False)

    analise = gerar_insight(
        indicador,
        texto
    )

    return {
        "indicador": indicador,
        "ranking": top10.to_dict(orient="records"),
        "insights": analise
    }
    