import matplotlib.pyplot as plt
from calc_moving_avg import moving_average as ma
import pandas as pd

def plot_ma_200days(stock):
    """
    Plot stock price and corresponding 200 day moving average 
    for a specified period of time

    Parameters
    ----------
    moving_avg : list
        A list representing the 200 day moving average of a stock price for
        the period of available data
        
    period : int
        period of time for which the plot is created

    Returns
    --------
    Altair Chart
        A line chart showing price data and corresponding 200 day 
        moving average line for a stock

    Examples
    --------
    >>> plot_ma_200days(moving_avg, 365)
    """

    data = pd.read_csv('data/'+stock+'.csv')
    data["Date"] = pd.to_datetime(data["Date"], utc=True).dt.date
    mov_avg = ma(stock, 200)  # always going to be 200

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

