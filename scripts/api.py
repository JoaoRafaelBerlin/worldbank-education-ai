from fastapi import FastAPI
import pandas as pd

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

    ranking = ranking.dropna(
        subset=["Melhor Valor"]
    )

    ranking = ranking.sort_values(
        by="Melhor Valor",
        ascending=False
    )

    top10 = ranking[
        ["Country Name", "Melhor Valor"]
    ].head(10)

    return top10.to_dict(orient="records")
    