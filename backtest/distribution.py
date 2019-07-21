import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from backtester import Backtester


if __name__ == "__main__":
    df = pd.read_csv('../data/returns.csv')
    df = df.dropna()
    df.set_index('date', inplace=True)
    a1 = {
        'sp500_adj_close': 0.5,
        'djia_adj_close': 0.5
    }
    bt = Backtester(df, allocation=a1, rebalance='m')
    bt.plot_return_distribution(years=10)
    plt.show()
