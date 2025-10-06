import streamlit as st
import yfinance as yf
import pandas as pd

st.title("📈 Einfacher Online Aktien-Bot")

ticker = st.text_input("Ticker (z. B. AAPL, TSLA)", "AAPL")
period = st.selectbox("Zeitraum", ["1y", "2y", "5y"], index=0)

if st.button("Daten laden"):
    data = yf.download(ticker, period=period)
    if data.empty:
        st.error("Keine Daten gefunden")
    else:
        st.write(f"{len(data)} Tage geladen für {ticker}")
        st.line_chart(data["Close"])
