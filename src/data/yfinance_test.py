from src.data.yfinance import Stock


def test_stock():
    stock = Stock("AAPL")
    assert stock.symbol == "AAPL"
    assert stock.stock.info["symbol"] == "AAPL"
    assert stock.stock.info["shortName"] == "Apple Inc."
    assert stock.stock.info["longBusinessSummary"] is not None
    assert stock.stock.info["longBusinessSummary"] != ""
    assert stock.get_price("1d", "1m") is not None
    assert stock.get_price("1d", "1m") != {}