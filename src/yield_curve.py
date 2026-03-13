# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:31:49 2026

@author: adrie
"""

#%%

import pandas as pd

data = pd.read_csv(r"D:\Swaption Pricer\Data\market_rates.csv")

maturities = data["maturity"].values
rates = data["rate"].values




#%% Class creation 
import numpy as np

class YieldCurve:

    def __init__(self, maturities, rates):

        self.maturities = maturities
        
        # calculation discount factors market points
        self.discount_factors = np.exp(-rates * maturities)

        # calculation log(DF)
        self.log_df = np.log(self.discount_factors)


    def discount_factor(self, t):

        # interpolation of log(DF)
        log_df_t = np.interp(t, self.maturities, self.log_df)

        # back to DF 
        return np.exp(log_df_t)


#%%
import matplotlib.pyplot as plt

# curve creation
curve = YieldCurve(maturities, rates)

# grid for figure
t_grid = np.linspace(min(maturities), max(maturities), 200)

df_curve = np.array([curve.discount_factor(t) for t in t_grid])

zero_rates = -np.log(df_curve) / t_grid


# plot
plt.figure(figsize=(8,5))

plt.plot(t_grid, zero_rates, label="Interpolated Yield Curve")
plt.scatter(maturities, rates, label="Market Points")

plt.xlabel("Maturity (years)")
plt.ylabel("Zero Rate")
plt.title("Yield Curve")
plt.legend()
plt.grid(True)

plt.savefig(r"D:\Swaption Pricer\Report\figures\yield_curve.pdf")
plt.show()


#%%







