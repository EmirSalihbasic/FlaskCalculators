from flask import Flask, render_template, request
from math import log, sqrt, exp, erf
from scipy.stats import norm


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("calculator.html")


@app.route("/", methods=["POST"])
def calculate():
    stock_price = float(request.form["stock_price"])
    strike_price = float(request.form["strike_price"])
    risk_free_rate = float(request.form["risk_free_rate"])
    time_to_maturity = float(request.form["time_to_maturity"])
    volatility = float(request.form["volatility"])

    d1 = (
        log(stock_price / strike_price)
        + ((risk_free_rate + (volatility**2) / 2) * time_to_maturity)
    ) / (volatility * sqrt(time_to_maturity))
    d2 = d1 - volatility * sqrt(time_to_maturity)

    call_price = stock_price * norm.cdf(d1) - strike_price * exp(
        -risk_free_rate * time_to_maturity
    ) * norm.cdf(d2)

    return render_template("calculator.html", result=call_price)


if __name__ == "__main__":
    app.run(debug=True)
