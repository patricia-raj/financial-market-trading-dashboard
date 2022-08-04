
import Tickers 
import pandas as pd
import hvplot.pandas
import numpy as np 
import matplotlib.pyplot as plt


def get_tickert_df(ticker):
    Tickers.readAllPriceCsv()
    ticker_df = Tickers.tickerPriceInfo[ticker]
    ticker_df.set_index('Date')
    ticker_df['YearMonth'] = pd.to_datetime(ticker_df['Date']).apply(lambda x: '{year}-{month}'.format(year=x.year, month=x.month))
    ticker_df['Year'] = pd.to_datetime(ticker_df['Date']).apply(lambda x: '{year}'.format(year=x.year))
    ticker_df['Month'] = pd.to_datetime(ticker_df['Date']).apply(lambda x: '{month}'.format(month=x.month))
    return ticker_df


ticker_df = get_tickert_df("AAPL")


def get_volume_line_plot(ticker_df):
    volume_mean_df = ticker_df.groupby(['Year', 'Date'])['Volume'].mean().sort_values()
    plt = volume_mean_df.hvplot.line(y='Date', x='Volume', by='Year', width=1000, height=500)
    return plt

ticker_df.hvplot(y='YearMonth', x='Close', by='Year', width=1000, height=500)
ticker_df.hvplot.barh(x='Date', y='Volume', groupby='YearMonth', width=1000, height=500) 

colors = {'red': '#ff207c', 'grey': '#42535b', 'blue': '#207cff', 'orange': '#ffa320', 'green': '#00ec8b'}
config_ticks = {'size': 14, 'color': colors['grey'], 'labelcolor': colors['grey']}
config_title = {'size': 18, 'color': colors['grey'], 'ha': 'left', 'va': 'baseline'}



def get_charts(stock_data):
    plt.rc('figure', figsize=(15, 10))
    
    fig, axes = plt.subplots(2, 1, 
                gridspec_kw={'height_ratios': [2, 1]})
    fig.tight_layout(pad=3)
    
    date = stock_data['YearMonth']
    close = stock_data['Close']
    vol = stock_data['Volume']
    adjclose = stock_data['Adj Close']
    
    plot_price = axes[0]
    plot_price.plot(date, close, color=colors['blue'], 
    linewidth=1, label='Price')
    plot_price.yaxis.tick_right()
    plot_price.tick_params(axis='both', **config_ticks)
    plot_price.set_ylabel('Price (in USD)', fontsize=14)
    plot_price.yaxis.set_label_position("right")
    plot_price.yaxis.label.set_color(colors['grey'])
    plot_price.grid(axis='y', color='gainsboro', linestyle='-', linewidth=0.5)
    plot_price.set_axisbelow(True)
    
    plot_vol = axes[1]
    plot_vol.bar(date, vol, width=1, color='green')
    plot_vol.yaxis.tick_right()
    plot_vol.tick_params(axis='both', **config_ticks)
    plot_vol.set_ylabel('Volume (in Millions)', fontsize=14)
    plot_vol.yaxis.set_label_position("right")
    plot_vol.yaxis.label.set_color(colors['grey'])
    plot_vol.grid(axis='y', color='gainsboro', linestyle='-', linewidth=0.5)
    plot_vol.set_axisbelow(True)


get_charts(ticker_df)



