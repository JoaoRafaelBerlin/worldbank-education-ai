import pandas as pd

# Ler o dataset original
df = pd.read_csv("data/raw/EdStatsData.csv")

print("Dataset carregado!")
print(df.shape)

# Remover linhas duplicadas
df = df.drop_duplicates()

print("Após remover duplicados:")
print(df.shape)

# Remover linhas sem país ou indicador
df = df.dropna(
    subset=[
        "Country Name",
        "Indicator Name"
    ]
)

print("Após remover nulos:")
print(df.shape)

# Indicadores escolhidos
indicadores = [
    "Adult literacy rate, population 15+ years, both sexes (%)",
    "Adult literacy rate, population 15+ years, female (%)",
    "Adult literacy rate, population 15+ years, male (%)",
    "Adjusted net enrolment rate, primary, both sexes (%)"
]

# Filtrar apenas os indicadores escolhidos
df = df[df["Indicator Name"].isin(indicadores)]

print("\nApós selecionar indicadores:")
print(df.shape)

# Mostrar as colunas disponíveis
print("\nColunas do dataset:")
print(df.columns.tolist())

# Selecionar apenas as colunas que vamos usar
colunas = [
    "Country Name",
    "Country Code",
    "Indicator Name",
    "Indicator Code",
    "2000",
    "2005",
    "2010",
    "2015"
]

df = df[colunas]

print("\nNovo formato do dataset:")
print(df.head())

# Salvar o dataset tratado
df.to_csv(
    "data/processed/education_clean.csv",
    index=False
)

print("\nArquivo education_clean.csv criado com sucesso!")
