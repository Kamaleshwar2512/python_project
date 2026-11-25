
from flask import Flask, render_template, request
from discount import calculate_discount

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    error = None

    if request.method == "POST":
        try:
            price = float(request.form.get("price", 0))
            discount_type = request.form.get("discount_type")
            discount_value = float(request.form.get("discount_value", 0))

            result = calculate_discount(
                price,
                discount_type,
                discount_value
            )

            result["percentage_saved"] = round(
                (result["discount"] / result["original_price"]) * 100,
                2
            )

        except (ValueError, TypeError):
            error = "Please enter valid values for all fields."

    return render_template(
        "index.html",
        result=result,
        error=error
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
