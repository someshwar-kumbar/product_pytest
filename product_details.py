def product_details(prod_id, name, quantity, price):
    result = (
        f"product ID:{prod_id}\n"
        f"product Name:{name}\n"
        f"Quantity:{quantity}\n"
        f"Price:{price}\n"
    )
    return result


if _name_ == "_main_":
    print(product_details(107, "iphone", 2, 70000))
