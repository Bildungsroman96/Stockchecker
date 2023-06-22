import yfinance as yf

def get_stock_data(ticker):
    stock = yf.Ticker(ticker)
    data = stock.history(period="1y")  # get data for the past year

    latest_close = data['Close'].iloc[-1]  # get the latest closing price
    low_52_week = data['Close'].min()  # get the lowest closing price in the past year

    # check if the latest closing price is the 52-week low
    if latest_close == low_52_week:
        print(f"The stock {ticker} is at its 52-week low!")
    else:
        print(f"The stock {ticker} is not at its 52-week low.")

get_stock_data("AAPL")
