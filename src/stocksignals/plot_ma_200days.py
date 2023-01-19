import matplotlib.pyplot as plt
from calc_moving_avg import moving_average as ma
import pandas as pd

def plot_ma_200days(stock_symbol):
    """
    Plot stock price and corresponding 200 day moving average.

    Parameters
    ----------        
    stock_symbol : string
        Ticker symbol of the stock for which the plot is created

    Returns
    --------
    Matplotlib chart
        A line chart showing price data and corresponding 200 day 
        moving average line for a stock.

    Examples
    --------
    >>> plot_ma_200days("MSFT")
    """

    data = pd.read_csv('data/'+stock_symbol+'.csv')
    data["Date"] = pd.to_datetime(data["Date"], utc=True).dt.date
    mov_avg = ma(stock_symbol, 200)  # always going to be 200

    plt.figure(figsize=(8,6))
    plt.plot(data.iloc[-200:, 0],  # date
             data.iloc[-200:, 4], "b-", label='Price')  # close
    plt.plot(mov_avg.iloc[-200:, 0],
             mov_avg.iloc[-200:, 1], "r--", label = '200-days SMA')
    plt.xticks(rotation=90)
    plt.xlabel("Date (YY-MM-DD)")
    plt.ylabel("Closing Price (USD)")
    plt.title("200 day moving average vs closing price")
    plt.legend()
    plt.show()

