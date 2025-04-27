from flask import blueprints
from src.data.yfinance import Stock
from flask import request
from flask import jsonify

endpoints = blueprints.Blueprint("endpoints", __name__)

@endpoints.route("/stock", methods=["POST"])
def get_stock():
    request_data = request.get_json()
    request_symbol = request_data.get("symbol")
    request_interval = request_data.get("interval")
    request_period = request_data.get("period")
    if request_symbol is None:
        return "No symbol provided"
    if request_interval is None:
        return "No interval provided"
    if request_period is None:
        return "No period provided"
    stock = Stock(request_symbol)
    return jsonify(stock.get_price(period=request_period, interval=request_interval))