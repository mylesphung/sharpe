# sharpe
 Program to calculate the Sharpe ratio of two stocks, compared to a benchmark (safer stock). The program uses 1-year data of the stocks and benchmark using Y-finance. The Sharpe ratio describes the performance of a stock compared to a benchmark, for each extra unit of risk taken on.
 
**Note:**
 While the Sharpe ratio is useful, especially for those with large portfolios, I don't recommend using it alone as an indicator of whether or not to buy a stock. A stock's past performance doesn't indicate future results.  
 
 Modules needed:
- pandas
- pandas_datareader
- numpy
- yfinance
- matplotlib.pyplot

 Caveats:
 - Can't input more than two stocks
 - Can't read stocks off a CSV chart- tickers have to be manually entered in
 - Ticker prices are based off of data from Y-finance, so the program's runtime is a lot slower if Y-finance is experiencing high traffic
