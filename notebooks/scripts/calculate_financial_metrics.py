from pynance import portfolio_optimizer as po
# Initialize the portfolio with tickers
def prepare_portfolio_data():
    tickers = ['AAPL', 'AMZN', 'GOOG', 'META', 'MSFT', 'NVDA', 'TSLA']
    portfolio = po.PortfolioCalculations(tickers)
    return portfolio

def calculate_pynance_metrics(portfolio):
    # Max Sharpe Ratio Portfolio
    max_sharpe_df = portfolio.max_sharpe_portfolio('df')
    print("Max Sharpe Ratio Portfolio Weights:\n", max_sharpe_df)
    
    # Min Variance Portfolio
    min_var_df = portfolio.min_var_portfolio('df')
    print("Min Variance Portfolio Weights:\n", min_var_df)
    
    # Expected Returns and Risks for Max Sharpe Portfolio
    risk_return = portfolio.max_sharpe_portfolio('rr')
    print("Expected Return and Risk for Max Sharpe Portfolio:\n", risk_return)
    
    # Efficient Frontier
    fig = portfolio.efficient_frontier()
    fig.show()
# calculate_pynance_metrics(portfolio)
