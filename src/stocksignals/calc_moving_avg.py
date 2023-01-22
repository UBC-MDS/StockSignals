import pandas as pd

def moving_average(stock_data, size):
    """
    Calculates the moving average of a stock price for a given range of dates

    Parameters
    ----------
    data : a data file containing all available stock data
            from Yahoo finance

    Returns
    --------
    moving_avg : dataframe
        A dataframe representing the 200 day moving average of a stock price.

    Examples
    --------
    >>> move_ave_200days(MSFT_data)
    """
    data = pd.read_csv('../../data/'+stock_data+'.csv')
    data.index = pd.to_datetime(data["Date"], utc=True).dt.date
    mov_avg = {}
    mov_avg[f"{size}MA"] = data["Close"].rolling(window=size).mean()
    moving_avg = pd.DataFrame(mov_avg).reset_index()
    return moving_avg