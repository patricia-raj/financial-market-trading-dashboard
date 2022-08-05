
# Import the required libraries
import numpy as np
import pandas as pd
import hvplot.pandas
from pathlib import Path
import streamlit as st
import Tickers
import holoviews as hv


st.markdown("# Industry Mectrics displaying Mean Close Costs and Volatility")
st.write("Each industry use 3 consistent selected tickers within the industry")
st.write("Averages reflect close prices at July 25")

industry = Tickers.sector_etf

Utilities_sector = Tickers.UTSEC
Telec = Tickers.Tele
Discres = Tickers.Disc
Staples = Tickers.Stp
Health = Tickers.Health
Basic = Tickers.BM
Indus = Tickers.Industrials
Tech = Tickers.Tech

dropdown = st.selectbox('Choose your industry', industry)

if dropdown == "Utilities Sector":
    st.line_chart(Utilities_sector.rolling(5).mean())
    st.line_chart(Utilities_sector.rolling(window=4).std())

if dropdown == "Telecomms Sector":
    st.line_chart(Telec.rolling(5).mean())
    st.line_chart(Telec.rolling(window=4).std())

if dropdown == "Basic Materials":
    st.line_chart(Basic.rolling(5).mean())
    st.line_chart(Basic.rolling(window=4).std())

if dropdown == "Consumer Discretion":
    st.line_chart(Discres.rolling(5).mean())
    st.line_chart(Discres.rolling(window=4).std())

if dropdown == "Consumer Staples":
    st.line_chart(Staples.rolling(5).mean())
    st.line_chart(Staples.rolling(window=4).std())

if dropdown == "Industrial":
    st.line_chart(Indus.rolling(5).mean())
    st.line_chart(Indus.rolling(window=4).std())

if dropdown == "Health":
    st.line_chart(Health.rolling(5).mean())
    st.line_chart(Health.rolling(window=4).std())

if dropdown == "Technology":
    st.line_chart(Tech.rolling(5).mean())
    st.line_chart(Tech.rolling(window=4).std())
