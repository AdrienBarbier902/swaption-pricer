# European Swaption Pricing Framework
## Yield Curve Construction and Valuation of a 2Y10Y European Swaption

## Overview

This project implements a simplified **interest rate derivatives pricing framework** in Python.

Starting from market interest rate data retrieved from the **European Central Bank (ECB) zero-coupon yield curve dataset**, the project constructs a yield curve, computes discount factors and forward swap rates, and prices a **European 2Y10Y payer swaption using the Black model**.

The objective of the project is to illustrate the full workflow used in interest rate derivatives markets, from **market data acquisition to derivative pricing and sensitivity analysis**.

---

# Project Workflow

The pricing framework follows the typical steps used in interest rate derivatives pricing:

1. Market Data Collection  
2. Yield Curve Construction  
3. Discount Factor Computation  
4. Forward Swap Rate Calculation  
5. Swaption Pricing using the Black Model  
6. Sensitivity Analysis  
7. Corporate Hedging Example  

---

# Project Structure

```
swaption-pricer
│
├── api
│   └── download_market_data.py
│
├── models
│   └── yield_curve.py
│
├── pricing
│   ├── swap.py
│   └── swaption.py
│
├── utils
│   └── math_utils.py
│
├── main.py
└── README.md
```

---

# Market Data

The interest rate data are retrieved from the **ECB zero-coupon yield curve dataset**.

| Maturity | Zero Rate |
|---------|-----------|
| 1Y | 2.25% |
| 2Y | 2.35% |
| 3Y | 2.41% |
| 5Y | 2.56% |
| 7Y | 2.74% |
| 10Y | 3.00% |
| 15Y | 3.29% |
| 20Y | 3.44% |
| 30Y | 3.47% |

These rates are used to construct the **yield curve** and derive discount factors.

---

# Discount Factors

Discount factors are computed using the continuous compounding formula:

$$
DF(t) = e^{-r(t)t}
$$

Example values:

| Maturity | Discount Factor |
|---------|----------------|
| 1Y | 0.9778 |
| 2Y | 0.9540 |
| 3Y | 0.9303 |
| 5Y | 0.8798 |
| 7Y | 0.8254 |
| 10Y | 0.7409 |

---

# Swap Annuity

The **swap annuity** represents the present value of the fixed leg payments of the swap.

$$
A = \sum_{i=1}^{n} \Delta_i DF(T_i)
$$

Where:

- $A$ : swap annuity  
- $DF(T_i)$ : discount factor at payment date $T_i$  
- $\Delta_i$ : accrual period between $T_{i-1}$ and $T_i$  
- $n$ : number of fixed leg payments  

---

# Forward Swap Rate

The forward swap rate represents the fixed interest rate that makes the value of an interest rate swap equal to zero at its start date.
In other words, it is the fixed rate that equates the present value of the fixed leg payments with the present value of the floating leg payments. This rate is the underlying variable used in the pricing of swaptions.

The swaption considered in this project is a **2Y10Y payer swaption**.

Meaning:

- Option maturity: **2 years**
- Underlying swap maturity: **10 years**
- Swap start: **2Y**
- Swap end: **12Y**
- Payment frequency: **semi-annual (0.5Y)**

The forward swap rate is computed as:

$$
S = \frac{DF(T_0) - DF(T_n)}{\sum_{i=1}^{n} \Delta_i DF(T_i)}
$$

Where:

- $S$ : forward swap rate  
- $DF(T)$ : discount factor at time $T$  
- $T_0$ : swap start date  
- $T_n$ : swap maturity  
- $T_i$ : payment date of coupon $i$  
- $\Delta_i$ : accrual period between $T_{i-1}$ and $T_i$  
- $n$ : number of fixed leg payments  

Results:

- **Forward Swap Rate ≈ 3.29%**
- **Swap Annuity ≈ 8.16**

---

# Swaption Pricing

The swaption price is computed using the **Black model**.

$$
Price = A \left( F N(d_1) - K N(d_2) \right)
$$

Where:

| Symbol | Meaning |
|------|---------|
| $F$ | Forward swap rate |
| $K$ | Strike rate |
| $A$ | Swap annuity |
| $N(\cdot)$ | Normal cumulative distribution |

The terms $d_1$ and $d_2$ are intermediate variables that capture the relationship between the forward swap rate, the strike rate, the volatility of the underlying rate and the time to maturity of the option.

$$
d_1 = \frac{\ln(F/K) + \frac{1}{2}\sigma^2 T}{\sigma \sqrt{T}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T}
$$

Where:

- $\sigma$ : volatility of the forward swap rate  
- $T$ : time to maturity of the swaption

Example parameters:

| Parameter | Value |
|-----------|-------|
| Forward Swap Rate | 3.29% |
| Strike | 3.29% (ATM) |
| Volatility | 20% |
| Swaption Price | 3.02% of notional |

---

# Sensitivity Analysis

## Volatility Sensitivity

| Volatility | Swaption Price |
|-----------|----------------|
| 10% | 1.51% |
| 15% | 2.27% |
| 20% | 3.02% |
| 25% | 3.77% |
| 30% | 4.51% |

Higher volatility increases the probability that the **forward swap rate exceeds the strike**, increasing the option value.

---

## Strike Sensitivity

Strike values are analysed around the **ATM forward rate ($F$)**.

| Strike | Swaption Price |
|-------|----------------|
| F - 1% | 8.46% |
| ATM ($F$) | 3.02% |
| F + 1% | 0.81% |

For a **payer swaption**, the price decreases as the strike increases.

---

# Corporate Hedging Example

Consider a corporate expecting to issue **EUR 100 million of debt in two years**.

The firm purchases a **2Y10Y payer swaption** to hedge against rising interest rates.

| Parameter | Value |
|----------|-------|
| Notional | EUR 100,000,000 |
| Swaption Premium | EUR 3,020,000 |
| Maximum Fixed Rate Locked (K) | 3.29% |
| Break-even Rate | 3.66% |

The break-even rate is the interest rate level at which the payoff from exercising the swaption exactly compensates for the premium paid.

Break-even rate:

$$
R_{BE} = K + \frac{Premium}{A \times N}
$$

If future interest rates exceed the break-even rate, the hedge becomes profitable.

---

# Limitations

This project uses a simplified framework:

- Basic yield curve interpolation
- Constant volatility assumption
- Black model dynamics

Possible extensions include:

- Yield curve bootstrapping
- Volatility surface calibration
- Hull–White interest rate model
- LIBOR Market Model (LMM)

---

# Author

Adrien Barbier
