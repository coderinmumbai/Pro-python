import yfinance as yf





msft = yf.Ticker("AAPL")



# get stock info

print(msft.info['open'])

print(msft.info['dayLow'])

print(msft.info['dayHigh'])

print(msft.info['currentPrice'])