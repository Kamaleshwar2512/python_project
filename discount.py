
def calculate_discount(price, discount_type, discount_value):

    if price <= 0:
        raise ValueError("Price must be greater than zero")

    if discount_value < 0:
        raise ValueError("Discount cannot be negative")

    if discount_type == "percentage":
        if discount_value > 100:
            raise ValueError("Percentage cannot exceed 100")
        discount = price * (discount_value / 100)

    elif discount_type == "fixed":
        discount = min(discount_value, price)

    else:
        raise ValueError("Invalid discount type")

    final_price = price - discount

    return {
        "original_price": round(price, 2),
        "discount": round(discount, 2),
        "final_price": round(final_price, 2)
    }
