#!/usr/bin/env python3

import pandas as pd

def swedish_and_foreigners():
    df1 = pd.read_csv("src/municipal.tsv", sep="\t", index_col=0)
    df = df1["Akaa": "Äänekoski"]

    print(df.loc["Eckerö"])
    mask = df["Share of Swedish-speakers of the population, %"]> 5
    mask2 =  df["Share of foreign citizens of the population, %"] > 5
    df_masked = df[mask]
    # print(df_masked[mask2].head()[["Population","Share of foreign citizens of the population, %", "Share of Swedish-speakers of the population, %"]])

    return df_masked[mask2][["Population", "Share of Swedish-speakers of the population, %", "Share of foreign citizens of the population, %"]]


def main():
    swedish_and_foreigners()

if __name__ == "__main__":
    main()
