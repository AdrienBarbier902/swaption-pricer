# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 15:33:00 2026

@author: adrie
"""
#%%
import numpy as np

def forward_swap_rate(curve, start, end, freq=0.5):

    # payment dates
    payment_dates = np.arange(start + freq, end + freq, freq)

    # annuity
    annuity = 0.0
    for t in payment_dates:
        df = curve.discount_factor(t)
        annuity += freq * df

    # DF start and end 
    df_start = curve.discount_factor(start)
    df_end = curve.discount_factor(end)

    # formula forward swap rate
    swap_rate = (df_start - df_end) / annuity

    return swap_rate, annuity




#%%
