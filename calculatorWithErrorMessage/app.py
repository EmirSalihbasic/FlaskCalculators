from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def calculator():
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            operation = request.form["operation"]

            if operation == "add":
                result = num1 + num2
                operator = "+"
            elif operation == "subtract":
                result = num1 - num2
                operator = "-"
            elif operation == "multiply":
                result = num1 * num2
                operator = "*"
            elif operation == "divide":
                result = num1 / num2
                operator = "/"
            else:
                raise ValueError("Invalid operation")

            return render_template(
                "calculator.html",
                num1=num1,
                num2=num2,
                operator=operator,
                result=result,
            )

        except (ValueError, ZeroDivisionError) as e:
            error_message = str(e)
            return render_template("calculator.html", error_message=error_message)

    return render_template("calculator.html")


if __name__ == "__main__":
    app.run(debug=True)
