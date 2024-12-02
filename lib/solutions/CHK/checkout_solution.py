

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Price table and special offers
    price_table = {
        "A": {"price": 50, "offer_quantity": 3, "offer_price": 130},
        "B": {"price": 30, "offer_quantity": 2, "offer_price": 45},
        "C": {"price": 20},
        "D": {"price": 15}
    }

    # Validate input
    if not isinstance(skus, str) or not skus.isalpha():
        return -1  # Return -1 for illegal input

    # Count the occurrences of each SKU
    item_counts = {}
    for sku in skus:
        if sku not in price_table:
            return -1  # Return -1 for illegal SKUs
        item_counts[sku] = item_counts.get(sku, 0) + 1

    # Calculate total price
    total_price = 0
    for sku, count in item_counts.items():
        item_price = price_table[sku]["price"]
        if "offer_quantity" in price_table[sku]:
            offer_quantity = price_table[sku]["offer_quantity"]
            offer_price = price_table[sku]["offer_price"]

            # Apply special offers
            total_price += (count // offer_quantity) * offer_price
            total_price += (count % offer_quantity) * item_price
        else:
            # No special offer, calculate based on individual price
            total_price += count * item_price

    return total_price

