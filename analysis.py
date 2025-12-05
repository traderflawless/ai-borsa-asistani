import yfinance as yf
import pandas as pd
import ta

def get_data(symbol, interval="1d", period="1mo"):
    data = yf.download(symbol, period=period, interval=interval)
    if data.empty:
        return None
    return data

def technical_analysis(symbol):
    df = get_data(symbol)

    if df is None:
        return "Veri alınamadı."

    df["rsi"] = ta.momentum.RSIIndicator(df["Close"]).rsi()
    df["macd"] = ta.trend.MACD(df["Close"]).macd()
    df["ema20"] = ta.trend.EMAIndicator(df["Close"], 20).ema_indicator()
    df["bb_high"] = ta.volatility.BollingerBands(df["Close"]).bollinger_hband()
    df["bb_low"] = ta.volatility.BollingerBands(df["Close"]).bollinger_lband()

    last = df.iloc[-1]

    result = f"""
📊 *{symbol} Teknik Analiz Sonucu*:

🔹 RSI: {round(last['rsi'],2)}
🔹 MACD: {round(last['macd'],2)}
🔹 EMA20: {round(last['ema20'],2)}
🔹 Bollinger Üst: {round(last['bb_high'],2)}
🔹 Bollinger Alt: {round(last['bb_low'],2)}

💡 *Yorum*:
"""

    # Kısa yorum ekle
    if last["rsi"] > 70:
        result += "Aşırı alım bölgesinde."
    elif last["rsi"] < 30:
        result += "Aşırı satım bölgesinde."
    else:
        result += "Nötr bölgede."

    return result
