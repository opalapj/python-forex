from pprint import pprint

import yfinance as yf


# Fetches quote (ticker) lookups from Yahoo Finance.
# The best way to find any information about the ticker of a currency
# you are interested in. You must enter the currency symbol according
# to the ISO-4217 standard.
lookup_results = yf.Lookup("PLN")
print(lookup_results.currency)
print(lookup_results.currency.index.values)
print(list(filter(lambda x: "EUR" in x, lookup_results.currency.index.values)))


# Fetches and organizes search results from Yahoo Finance, including
# stock quotes and news articles.
search_results = yf.Search("PLN")
quotes = search_results.quotes
for quote in quotes:
    print(f"{quote["longname"]} -> {quote["symbol"]}")


# More or less interesting market data.
currencies = yf.Market("CURRENCIES")
currencies.summary["CCY"]["fullExchangeName"]
currencies.summary["CCY"]["quoteType"]


# The Ticker module, allows you to access ticker data in a Pythonic way.
ticker = yf.Ticker("EURPLN=X")
tickers = yf.Tickers("EURPLN=X")
pprint(ticker.info)


# Several ways to download time series.
ticker.history()
tickers.history()
tickers.download()
yf.download('EURPLN=X')


# https://ranaroussi.github.io/yfinance/reference/yfinance.price_history.html#yfinance.scrapers.history.PriceHistory.history
time_series = ticker.history(
    start="2025-01-01",  # inclusive
    end="2026-01-01",  # exclusive
    interval="1d",  # Valid intervals: 1m,2m,5m,15m,30m,60m,90m,1h,1d,5d,1wk,1mo,3mo
)
print(time_series)
