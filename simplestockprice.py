import yfinance as yf
import streamlit as st

st.write("""
# Stock Price Web App

""")
st.text("Gamestop Stock Price")

tickerData = yf.Ticker("GME")

tickerDf = tickerData.history(period='1d', start='2021-1-1', end='2021-2-5')

st.subheader("Closing Price")
st.line_chart(tickerDf.Close)
st.subheader("Volume Price")
st.line_chart(tickerDf.Volume)


#st.subheader(tickerData.info['longBusinessSummary'])
st.subheader("Analysts recommendations")
st.text(tickerData.recommendations)
