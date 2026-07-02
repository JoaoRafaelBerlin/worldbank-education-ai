import pandas as pd

arquivo = "data/raw/EdStatsData.csv"

df = pd.read_csv(arquivo)

print("Linhas:", df.shape[0])
print("Colunas:", df.shape[1])

print("\nColunas do dataset:\n")

for coluna in df.columns:
    print(df.head())
    print("\nQuantidade de países:")
    print(df["Country Name"].nunique())
    print("\nQuantidade de indicadores:")
    print(df["Indicator Name"].nunique())
    print("\nPrimeiros países:\n")
    print(df["Country Name"].unique()[:20])

    paises = pd.DataFrame(df["Country Name"].unique(), columns=["Pais"])

paises.to_csv(
    "data/output/paises.csv",
    index=False
)

indicadores = pd.DataFrame(
    df["Indicator Name"].unique(),
    columns=["Indicador"]
)

indicadores.to_csv(
    "data/output/indicadores.csv",
    index=False
)

print("\nArquivos gerados com sucesso!")