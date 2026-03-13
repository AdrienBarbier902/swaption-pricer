# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:54:24 2026

@author: adrie
"""

#%%

import pandas as pd

# maturités que l'on veut récupérer
urls = {
    1: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_1Y?format=csvdata",
    2: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_2Y?format=csvdata",
    3: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_3Y?format=csvdata",
    5: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_5Y?format=csvdata",
    7: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_7Y?format=csvdata",
    10: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_10Y?format=csvdata",
    15: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_15Y?format=csvdata",
    20: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_20Y?format=csvdata",
    30: "https://data-api.ecb.europa.eu/service/data/YC/B.U2.EUR.4F.G_N_A.SV_C_YM.SR_30Y?format=csvdata"
}

rates = []

for maturity, url in urls.items():

    try:

        df = pd.read_csv(url)

        latest_rate = df["OBS_VALUE"].iloc[-1] / 100

        rates.append({
            "maturity": maturity,
            "rate": latest_rate
        })

    except Exception as e:

        print(f"Erreur pour la maturité {maturity}Y :", e)

rates_df = pd.DataFrame(rates)

rates_df = rates_df.sort_values("maturity")

rates_df.to_csv("D:\Swaption Pricer\Data\market_rates.csv", index=False)

print("Downloaded Market data :")
print(rates_df)

#%%











#%%