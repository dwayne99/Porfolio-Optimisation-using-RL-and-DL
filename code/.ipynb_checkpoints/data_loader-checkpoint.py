import pandas as pd

# Data
from yahoofinancials import YahooFinancials

# Create an empty DataFrame to store the closing prices
def get_closing_prices(tickers, start_date, end_date, time_interval):
    closing_prices = pd.DataFrame()

    # Loop through each ticker
    for ticker in tickers:
        # Fetch the historical prices for the ticker
        yahoo_financials = YahooFinancials(ticker, country="US")
        historical_data = yahoo_financials.get_historical_price_data(start_date, end_date, time_interval)

        # Extract the closing prices
        dates = [x['formatted_date'] for x in historical_data[ticker]['prices']]
        closes = [x['close'] for x in historical_data[ticker]['prices']]

        # Create a DataFrame for the current ticker
        df = pd.DataFrame({'Date': dates, ticker: closes})
        df['Date'] = pd.to_datetime(df['Date'])
        df.set_index('Date', inplace=True)

        # Merge the current DataFrame into the main DataFrame
        if closing_prices.empty:
            closing_prices = df
        else:
            closing_prices = pd.merge(closing_prices, df, left_index=True, right_index=True, how='outer')

    return closing_prices
    