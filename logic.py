# logic.py

import yfinance as yf
import numpy as np

def interpret_results(mean, std_dev):
    interpretation = ""

    # Mean return interpretation
    if mean > 0:
        interpretation += "The stock has a positive average return. "
    else:
        interpretation += "The stock has a negative or weak average return. "

    # Volatility interpretation
    if std_dev < 0.01:
        interpretation += "It is very stable with low volatility. "
    elif std_dev < 0.03:
        interpretation += "It shows moderate fluctuations. "
    else:
        interpretation += "It is highly volatile with large price swings. "

    # Combined insight
    if mean > 0 and std_dev < 0.02:
        interpretation += "This suggests a relatively good risk-return balance."
    elif mean > 0 and std_dev > 0.03:
        interpretation += "Returns are high but come with significant risk."
    else:
        interpretation += "The stock may not offer an attractive risk-return profile."

    return interpretation

def get_stock_data(symbol, period="3mo"):
    stock = yf.Ticker(symbol)
    data = stock.history(period=period)
    return data["Close"].dropna().values


def compute_returns(prices):
    returns = []
    for i in range(1, len(prices)):
        r = (prices[i] - prices[i - 1]) / prices[i - 1]
        returns.append(r)
    return np.array(returns)


def calculate_statistics(returns):
    mean = np.mean(returns)
    variance = np.var(returns)
    std_dev = np.sqrt(variance)
    max_return = np.max(returns)
    min_return = np.min(returns)

    return mean, variance, std_dev, max_return, min_return


def classify_risk(std_dev):
    if std_dev < 0.01:
        return "Low Risk"
    elif std_dev < 0.03:
        return "Medium Risk"
    else:
        return "High Risk"


def probability_range(mean, std_dev):
    lower = mean - 2 * std_dev
    upper = mean + 2 * std_dev
    return lower, upper
