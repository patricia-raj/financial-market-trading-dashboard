
# Import the required libraries
import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
import streamlit as st
import Tickers
import holoviews as hv


st.markdown("# DMAC Trading Signal")
st.sidebar.markdown("## Select Ticker for Algo Strategy")

ticker_algo = st.sidebar.selectbox("Select the ticker", Tickers.nasdaq_100)

# Read the csv file from the Resources folder into a Pandas DataFrame
# Set the `Date` column as the DateTimeIndex
trading_df = pd.read_csv(
    Path('Resources/NASDQ-100-Tickers/' + ticker_algo + '.csv'), 
    index_col="Date",
    parse_dates=True, 
    infer_datetime_format=True
)


# Create a DataFrame filtering only the index and Close columns
signals_df = trading_df.loc[:,["Close"]]


# Set the short_window (50) and long window (100) variables
short_window = 25
long_window = 50


# Generate the short and long moving averages (50 and 100 days, respectively)
signals_df['SMA25'] = signals_df['Close'].rolling(window=short_window).mean()
signals_df['SMA50'] = signals_df['Close'].rolling(window=long_window).mean()

# Initialize the new Signal column to hold the trading signal
signals_df['Signal'] = 0.0


# Generate the trading signal 0 or 1,
# where 1 is the short-window (SMA50) is less than the long-window (SMA100)
signals_df["Signal"][short_window:] = np.where(
    signals_df["SMA25"][short_window:] < signals_df["SMA50"][short_window:], 1.0, 0.0
)


# Calculate the points in time at which a position should be taken, 1 or -1
signals_df['Entry/Exit'] = signals_df['Signal'].diff()


### ROI Calcs ###
signals_df["cost/proceeds"] = 0
share_size = 100


for index, row in signals_df.iterrows():
    if row['Entry/Exit'] == 1:
         signals_df.loc[index, "cost/proceeds"] = -(row["Close"] * share_size)
    elif row['Entry/Exit'] == -1:
        signals_df.loc[index, "cost/proceeds"] = (row["Close"] * share_size)
    else:
        signals_df.loc[index, "cost/proceeds"] = 0
            

        
# Visualize entry positions relative to close price
entry = signals_df[signals_df['Entry/Exit'] == 1.0]['Close'].hvplot.scatter(
    color='green',
    marker='^',
    legend=False,
    ylabel='Price in $',
    width=1500,
    height=400)



# Visualize exit positions relative to close price
exit = signals_df[signals_df['Entry/Exit'] == -1.0]['Close'].hvplot.scatter(
    color='red',
    marker='v',
    legend=False,
    ylabel='Price in $',
    width=1500,
    height=400)



# Visualize Close price for the investment
security_close = signals_df[['Close']].hvplot(
    line_color='lightgray',
    ylabel='Price in $',
    width=1500,
    height=400)

# Visualize the SMA50 and SMA 100 moving averages
moving_avgs = signals_df[['SMA25', 'SMA50']].hvplot(
    ylabel='Price in $',
    width=1500,
    height=400)



# Overlay all four plots in a single visualization
entry_exit_plot = security_close * moving_avgs * entry * exit
entry_exit_plot.opts(
    title="Short-Position Dual Moving Average Trading Algorithm"
)

entry_exit_plot = hv.render(entry_exit_plot)

st.bokeh_chart(entry_exit_plot, use_container_width=True)

# Calculate the total profit/loss for 100 share size orders
total_profit_loss = round(signals_df["cost/proceeds"].sum(), 2)

# Print the profit/loss metrics
st.markdown("### Algo Strategy PnL")
st.write(f"The total profit/loss of the trading strategy is ${total_profit_loss}.")


# Initialize the variable to hold the value of the invested capital
invested_capital = 0


# Calculate the invested capital by adding the cost of all buy trades
for index, row in signals_df.iterrows():
    if row['Entry/Exit'] == 1:
        invested_capital = invested_capital + row["cost/proceeds"]



# Calculate the return on investment (ROI)
roi = round((total_profit_loss / -(invested_capital)) * 100, 2)
         
# Print the ROI
st.markdown("### Algo Strategy ROI")
st.write(f"The trading algorithm resulted in a return on investment of {roi}%")


