import streamlit as st
import yfinance as yf
import pandas as pd
import Tickers 

st.set_page_config(layout='wide')
st.title('Real-Time - Cumulative Return and Volume Comparison' )
tickers = Tickers.nasdaq_100

dropdown = st.multiselect( 'Pick vour assets', tickers)
start = st.date_input('Start',value = pd.to_datetime('2021-01-01'))
end = st.date_input ('End', value = pd.to_datetime('today'))

def relativeret(df):
    rel = df.pct_change()
    cumret = (1+rel).cumprod() - 1
    cumret = cumret.fillna(0)
    return cumret


if len (dropdown) > 0:
    close_df = yf.download(dropdown,start,end)['Close']
    return_df = relativeret(close_df)
    st.header('Returns of {}'.format(dropdown))
    st.line_chart(return_df,width=1000, height=500, use_container_width=True)
    
    
    volume_df = yf.download(dropdown,start,end)['Volume']
    st.header('Volume of {}'.format(dropdown))
    st.bar_chart(volume_df,width=1000, height=500, use_container_width=True)