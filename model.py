import yfinance as yf
import pandas as pd
import numpy as np
#import pandas_datareader as pdr
import matplotlib.pyplot as plt



# This function gets data for the ticker from yahoo finance and return the data from the start to end date
def get_stock_data(ticker, start_date, end_date):
    # ticker = stock name, start date and end date = 'YYYY-MM-DD'
    stock_data = yf.download(ticker, start=start_date, end=end_date)
    stock_data.reset_index(inplace=True)
    return stock_data

def plot_stock_data(stock_data):
    plt.figure(figsize=(14, 7))
    plt.plot(stock_data['Date'], stock_data['Close'], label='Close Price')
    plt.title('Stock Price Over Time')
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.legend()
    plt.grid()
    plt.show()