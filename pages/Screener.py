import streamlit as st
import Tickers
import pandas as pd


def generateDf(columnList, rowList):
    df = pd.DataFrame(rowList, columns=columnList)
    df = df.set_index('Ticker')
    return df

#
# Streamlit code:
#
st.markdown("# Stock screener ❄️")
st.sidebar.markdown("# Screener categories ❄️")
st.markdown("### Testing stocks in the nasdaq 100...")


#
# Walk through the nasdaq 100 & create an entry for each:
#
columnList = ['Ticker', 'Close', 'Week%', 'Month%', 'YTD%', 'Year%']
rowList = []
for ticker in Tickers.nasdaq_100:
    
    #weekly_pct_change = Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'].pct_change(periods = 1)

    weekly_pct_change = (Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'] -
                          Tickers.tickerPriceInfo[ticker].iloc[-6]['Close']) * 100 / Tickers.tickerPriceInfo[ticker].iloc[-1]['Close']
    
    monthly_pct_change = (Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'] -
                          Tickers.tickerPriceInfo[ticker].iloc[-22]['Close']) * 100 / Tickers.tickerPriceInfo[ticker].iloc[-1]['Close']

    #ytd_pct_change = (Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'] -
    #                  Tickers.tickerPriceInfo[ticker].iloc[-22]['Close']) * 100 / Tickers.tickerPriceInfo[ticker].iloc[-1]['Close']

    ytd_pct_change = 0;

    yearly_pct_change = 0;



    l = [ticker, Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'],
         round(weekly_pct_change, 2),
         round(monthly_pct_change, 2),
         round(ytd_pct_change, 2),
         round(yearly_pct_change,2)]
    rowList.append(l)

df = generateDf(columnList, rowList)

st.table(df)
