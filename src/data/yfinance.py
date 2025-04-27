import yfinance as yf
from typing import Dict

class Stock:
    def __init__(self, symbol:str) -> None:
        self.symbol = symbol
        self.stock = yf.Ticker(symbol)

    def get_price(self, period:str, interval:str) -> Dict:
        df = self.stock.history(period=period, interval=interval)
        df.index = df.index.strftime('%Y-%m-%d %H:%M:%S')
        df["Time"] = df.index
        return df.to_dict()