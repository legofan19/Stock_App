from model import get_stock_data, plot_stock_data

data = get_stock_data('AAPL', '2014-01-01', '2020-12-31')

plot_stock_data(data)