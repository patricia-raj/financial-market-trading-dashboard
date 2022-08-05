import streamlit as st
import yfinance as yf
import pandas as pd
import Tickers 
import html5lib
import requests
import uuid
import matplotlib.pyplot as plt
import altair as alt

st.set_page_config(layout='wide')
st.title('Real-Time: Major Indices')

start = st.date_input('Start',value = pd.to_datetime('2010-01-01'))
end = st.date_input ('End', value = pd.to_datetime('today'))

region_idx= { 'US & Canada' : ['^GSPC', '^DJI', '^IXIC', '^RUT','^GSPTSE'],
             'Latin America' : ['^BVSP', '^MXX', '^IPSA'],
             'East Asia' : ['^N225', '^HSI', '000001.SS', '399001.SZ', '^TWII', '^KS11'],
             'ASEAN & Oceania' : ['^STI', '^JKSE', '^KLSE','^AXJO',  '^NZ50'],
             'South & West Asia' : ['^BSESN', '^TA125.TA'],
             'Europe' : ['^FTSE', '^GDAXI', '^FCHI', '^STOXX50E','^N100', '^BFX']
            }


url = 'https://finance.yahoo.com/world-indices'
cookies = {'euConsentId': str(uuid.uuid4())}
html = requests.get(url, cookies=cookies).content
majorStockIdx = pd.read_html(html)[0]
majorStockIdx.drop(['Intraday High/Low', '52 Week Range', 'Day Chart'], axis=1, inplace=True)

stock_list = []
for stock in majorStockIdx.Symbol: 
    ticker_data = yf.Ticker(stock)
    ticker_df = ticker_data.history(period='1d', start=start, end=end)
    ticker_df['ticker'] = stock 
    stock_list.append(ticker_df)

master_stock_idx = pd.concat(stock_list, axis = 0)

def getRegionTickerKey(ticker):
    for k in region_idx.keys():
        if ticker in region_idx[k]:
            return k
master_stock_idx['Region']= master_stock_idx.ticker.apply(lambda x: getRegionTickerKey(x))

master_stock_idx.drop('Adj Close', axis=1, inplace=True)
master_stock_idx = master_stock_idx[master_stock_idx['Region'].notnull()]


master_stock_idx['Returns'] = ((1 + master_stock_idx['Close'].pct_change()).cumprod() - 1)
master_stock_idx['Returns'] = master_stock_idx.Returns.fillna(method='bfill')

returns_df = master_stock_idx.groupby(['Date', 'ticker'])['Returns'].first().unstack()
returns_df = returns_df.fillna(method='bfill')

usa_df = master_stock_idx.loc[master_stock_idx.ticker.isin(['^GSPC','^IXIC','^DJI','^RUT'])][['ticker','Region','Returns']]
usa_df = usa_df.groupby(['Date', 'ticker'])['Returns'].first().unstack()

st.header("US Region Major Stock Indices")
with st.container():
   
    col_nas, col_dow = st.columns(2)
    
    with col_nas:
        st.subheader("NASDAQ-(^IXIC)")
        st.metric((majorStockIdx.loc[majorStockIdx.Symbol == '^IXIC']['Last Price'].to_string())+" (Last Price)", majorStockIdx.loc[majorStockIdx.Symbol == '^IXIC']['Change'].to_string().split("   ")[1], majorStockIdx.loc[majorStockIdx.Symbol == '^IXIC']['% Change'].to_string().split("   ")[1])
        st.line_chart(usa_df['^IXIC'], width=1000, height=500, use_container_width=True)

    with col_dow:
        st.subheader("Dow Jones-(^DJI)")
        st.metric((majorStockIdx.loc[majorStockIdx.Symbol == '^DJI']['Last Price'].to_string())+" (Last Price)", majorStockIdx.loc[majorStockIdx.Symbol == '^DJI']['Change'].to_string().split("   ")[1], majorStockIdx.loc[majorStockIdx.Symbol == '^DJI']['% Change'].to_string().split("   ")[1])
        st.line_chart(usa_df['^DJI'], width=1000, height=500, use_container_width=True)

with st.container():
    
    col_sp500, col_rus = st.columns(2)

    with col_sp500:
        st.subheader("S&P 500-(^GSPC)")
        st.metric((majorStockIdx.loc[majorStockIdx.Symbol == '^GSPC']['Last Price'].to_string())+" (Last Price)", majorStockIdx.loc[majorStockIdx.Symbol == '^GSPC']['Change'].to_string().split("   ")[1], majorStockIdx.loc[majorStockIdx.Symbol == '^GSPC']['% Change'].to_string().split("   ")[1])
        st.line_chart(usa_df['^GSPC'], width=1000, height=500, use_container_width=True)
    
    with col_rus:
        st.subheader("Russell-(^RUT)")
        st.metric((majorStockIdx.loc[majorStockIdx.Symbol == '^RUT']['Last Price'].to_string())+" (Last Price)", majorStockIdx.loc[majorStockIdx.Symbol == '^RUT']['Change'].to_string().split("   ")[1], majorStockIdx.loc[majorStockIdx.Symbol == '^RUT']['% Change'].to_string().split("   ")[1])
        st.line_chart(usa_df['^RUT'], width=1000, height=500, use_container_width=True)
    

st.header("World Major Stock Indices")
st.dataframe(majorStockIdx)

st.header("World Major Stock Indices - Comparison")
fig, axes = plt.subplots(3,2, figsize=(12, 8),sharex=True)
colors = ["#965757", "#D67469", "#4E5A44", "#A1B482", '#EFE482', "#99BFCF"] 
for i, k in enumerate(region_idx.keys()):
    ax = axes[int(i/2), int(i%2)]
    for j,t in enumerate(region_idx[k]):
        ax.plot(returns_df.index, returns_df[t], marker='', linewidth=1, color = colors[j])
        ax.legend([t for t in region_idx[k]], loc='upper left', fontsize=7)
        ax.set_title(k, fontweight='bold')
fig.text(0.5,0, "Year", ha="center", va="center", fontweight ="bold")
fig.text(0,0.5, "Price Change/Return (%)", ha="center", va="center", rotation=90, fontweight ="bold")
fig.suptitle("Price Change/Return for Major Stock Indices", fontweight ="bold",y=1.05, fontsize=14)
fig.tight_layout()
st.pyplot(fig)

