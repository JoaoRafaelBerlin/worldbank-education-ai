import pandas as pd


def carregar_dados():
    return pd.read_csv("data/processed/education_clean.csv")


def mostrar_indicadores(df):

    indicadores = sorted(df["Indicator Name"].unique())

    print("\nIndicadores disponíveis:\n")

    for i, indicador in enumerate(indicadores, start=1):
        print(f"{i} - {indicador}")

    return indicadores


def escolher_indicador(indicadores):

    opcao = int(input("\nDigite o número do indicador: "))
    return indicadores[opcao - 1]


def escolher_paises():

    pais1 = input("\nDigite o primeiro país: ")
    pais2 = input("Digite o segundo país: ")

    return pais1, pais2


def comparar_paises(df, indicador, pais1, pais2):

    resultado = df[
        (df["Indicator Name"] == indicador) &
        (df["Country Name"].isin([pais1, pais2]))
    ]

    print("\nResultado da comparação\n")

    anos = ["2000", "2005", "2010", "2015"]

    for _, linha in resultado.iterrows():

        print("-" * 50)
        print("País:", linha["Country Name"])

        for ano in anos:

            valor = linha[ano]

            if pd.isna(valor):
                print(f"{ano}: Sem informação")
            else:
                print(f"{ano}: {valor:.2f}")


def gerar_ranking(df, indicador):

    print("\n")
    print("=" * 60)
    print("TOP 10 PAÍSES")
    print("=" * 60)

    ranking = df[df["Indicator Name"] == indicador].copy()

    ranking["Melhor Valor"] = ranking[
        ["2000", "2005", "2010", "2015"]
    ].max(axis=1)

    ranking = ranking.dropna(subset=["Melhor Valor"])

    ranking = ranking.sort_values(
        by="Melhor Valor",
        ascending=False
    )

    print(
        ranking[
            ["Country Name", "Melhor Valor"]
        ].head(10)
    )


def main():

    print("=" * 60)
    print("AGENTE DE INTELIGÊNCIA GLOBAL EM EDUCAÇÃO")
    print("=" * 60)

    df = carregar_dados()

    indicadores = mostrar_indicadores(df)

    indicador = escolher_indicador(indicadores)

    print("\nIndicador escolhido:")
    print(indicador)

    pais1, pais2 = escolher_paises()

    comparar_paises(df, indicador, pais1, pais2)

    gerar_ranking(df, indicador)


if __name__ == "__main__":
    main()