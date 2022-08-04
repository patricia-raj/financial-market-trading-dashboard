import streamlit as st
import Tickers
import Volume_ClosePrice
import holoviews as hv

st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

nasdaq_100 = st.sidebar.selectbox("Select the market cap", Tickers.nasdaq_100)
df= Volume_ClosePrice.get_tickert_df("AAPL")

nice_plot = Volume_ClosePrice.get_volume_line_plot(df)
st.bokeh_chart((hv.render(nice_plot, backend='bokeh'))
               
