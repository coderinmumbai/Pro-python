import yfinance as yf

choice = input("Write a stock symbol: ") #SYMBOL IS GOOG


choice = choice.upper()

data = yf.download(tickers=choice, period = '1d', interval = '15m', rounding= True)

print(data)