# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:33:19 2026

@author: adrie
"""
#%% Black Formula Pricing 

import numpy as np
from scipy.stats import norm


def black_swaption(F, K, sigma, T, annuity):

    # d1
    d1 = (np.log(F / K) + 0.5 * sigma**2 * T) / (sigma * np.sqrt(T))

    # d2
    d2 = d1 - sigma * np.sqrt(T)

    # Black formula
    price = annuity * (F * norm.cdf(d1) - K * norm.cdf(d2))

    return price



#%%




#%%
