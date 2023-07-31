import pandas as pd

# Tickers of the Stocks to examine within the portfolio
# tickers = ['META.L','AMZN.L','AAPL', 'GOOG', 'NFLX', 'MSFT', 'TSLA']
# tickers = ['META', 'AMZN', 'AAPL', 'GOOG', 'NFLX', 'MSFT', 'TSLA', 'BP', 'GSK', 'RIO', 'AAL', 'AZN', 'PRU', 'VOD', 'BHP', 'NG', 'WPP']
# tickers = "BP.L SHEL.L SSE.L HSBA.L LLOY.L STAN.L TSCO.L SBRY.L MKS.L GSK.L AZN.L HIK.L SGE.L SCT.L SXS.L RR.L SMIN.L WEIR.L VOD.L BT-A.L ULVR.L DGE.L RKT.L BBY.L COST.L MGNS.L"
# tickers = "SHEL.L ULVR.L HSBA.L BP.L AZN.L GSK.L BATS.L DGE.L RIO.L RKT.L LLOY.L VOD.L"
# # Selecting the top-10 mid-cap stocks
# tickers = "TTWO SIX ALK JBLU JACK LYV DISH ZG"


# Data
from yahoofinancials import YahooFinancials

# Create an empty DataFrame to store the closing prices
def get_closing_prices(tickers, start_date, end_date, time_interval):
    closing_prices = pd.DataFrame()

    # Loop through each ticker
    for ticker in tickers:
        # Fetch the historical prices for the ticker
        yahoo_financials = YahooFinancials(ticker, country="US")
        try:
            historical_data = yahoo_financials.get_historical_price_data(start_date, end_date, time_interval)

            # Extract the closing prices
            dates = [x['formatted_date'] for x in historical_data[ticker]['prices']]
            closes = [x['close'] for x in historical_data[ticker]['prices']]
        except:
            print(ticker)

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
    