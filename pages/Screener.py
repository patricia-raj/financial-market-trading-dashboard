import streamlit as st
import Tickers
import pandas as pd

pd.set_option('display.precision', 2)

def setCellBgColor(cellValue):
    bgRed = 'background-color: darkorange;'
    bgGreen = 'background-color: lightgreen;'
    default = ''

    if type(cellValue) in [float]:
        if (cellValue > 0):
            return bgGreen
        elif (cellValue < 0):
            return bgRed

    return default


def generateDf(columnList, rowList):
    df = pd.DataFrame(rowList, columns=columnList)
    df = df.set_index('Ticker')
    return df

#
# Streamlit code:
#
st.markdown("# Stock screener (Nasdaq 100)❄️")
st.sidebar.markdown("# Screener categories ❄️")
st.sidebar.markdown("# Display Options ❄️")

#
# Create a checkbox & store it in a list
#
chWeek = st.sidebar.checkbox('Week', value=True)
chMonth = st.sidebar.checkbox('Month', value=True)
chYtd = st.sidebar.checkbox('Ytd', value=True)
chYear = st.sidebar.checkbox('Year', value=True)
chOptions = {"Week%" : chWeek, "Month%" : chMonth,
             "YTD%" : chYtd, "Year%" : chYear}

maxRowCount = st.sidebar.slider('Max tickers to display',
                                min_value = 1, max_value = 102, value = 25)

#
# Walk through the nasdaq 100 & create an entry for each:
#
columnList = ['Ticker', 'Close', 'Week%', 'Month%', 'YTD%', 'Year%']
rowList = []
for ticker in Tickers.nasdaq_100:
    weekly_pct_change = (Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'] -
                          Tickers.tickerPriceInfo[ticker].iloc[-6]['Close']) * 100 / Tickers.tickerPriceInfo[ticker].iloc[-1]['Close']

    monthly_pct_change = (Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'] -
                          Tickers.tickerPriceInfo[ticker].iloc[-22]['Close']) * 100 / Tickers.tickerPriceInfo[ticker].iloc[-1]['Close']

    ytd_pct_change = (Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'] -
                         Tickers.tickerPriceInfo[ticker].iloc[-138]['Close']) * 100 / Tickers.tickerPriceInfo[ticker].iloc[-1]['Close']

    yearly_pct_change = (Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'] -
                         Tickers.tickerPriceInfo[ticker].iloc[-252]['Close']) * 100 / Tickers.tickerPriceInfo[ticker].iloc[-1]['Close']

    l = [ticker, Tickers.tickerPriceInfo[ticker].iloc[-1]['Close'],
         weekly_pct_change,
         monthly_pct_change,
         ytd_pct_change,
         yearly_pct_change]
    rowList.append(l)

df = generateDf(columnList, rowList)

#
# Check the display options & modify accrodindly
#
for key, value in chOptions.items():
    if (0 == value):
        df = df.drop([key], axis = 1)

df = df[0: maxRowCount]
df = df.style.applymap(setCellBgColor, subset = df.columns[1:])

st.table(df)
