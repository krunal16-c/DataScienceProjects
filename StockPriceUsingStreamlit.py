
import yfinance as yf
import streamlit as st
import pandas as pd

st.write(
    """
    # Simple Stock price app

    Shown are the stock **closing price** and **volume** of Google!


    """
)

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period="1d", start="2015-05-31", end="2025-5-31")

st.write("""
## Closing price 

""")

st.line_chart(tickerDf.Close)

st.write("""
## Volume Price
""")

st.line_chart(tickerDf.Volume)
