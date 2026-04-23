# ui.py

import matplotlib.pyplot as plt
import numpy as np


def plot_price(prices):
    fig, ax = plt.subplots()
    ax.plot(prices)
    ax.set_title("Stock Price Over Time")
    ax.set_xlabel("Days")
    ax.set_ylabel("Price")
    ax.grid()
    return fig


def plot_returns_with_curve(returns, mean, std_dev):
    fig, ax = plt.subplots()

    # Histogram
    ax.hist(returns, bins=40, density=True, alpha=0.5)

    # Normal distribution curve
    x = np.linspace(min(returns), max(returns), 200)
    y = (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2)

    ax.plot(x, y)
    ax.axvline(mean, linestyle='dashed', linewidth=2)

    ax.set_title("Returns Distribution")
    ax.set_xlabel("Returns")
    ax.set_ylabel("Density")
    ax.grid()

    return fig
 
