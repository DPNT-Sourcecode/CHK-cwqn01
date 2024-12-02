# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    # Price table and special offers
    price_table = {
        "A": {"price": 50, "offers": [(5, 200), (3, 130)]},
        "B": {"price": 30, "offers": [(2, 45)]},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "special_offer": {"requires": 2, "free_item": "B", "free_count": 1}},
    }

    # Validate input
    if not isinstance(skus, str):
        return -1  # Return -1 for illegal input
    if skus == "":  # If input is an empty string, return 0
        return 0

    # Count the occurrences of each SKU
    item_counts = {}
    for sku in skus:
        if sku not in price_table:
            return -1  # Return -1 for illegal SKUs
        item_counts[sku] = item_counts.get(sku, 0) + 1

    # Apply special offers and calculate total price
    total_price = 0
    free_items = {}

    for sku, count in item_counts.items():
        item_info = price_table[sku]
        item_price = item_info["price"]

        # Handle "2E get one B free"
        if sku == "E" and "special_offer" in item_info:
            special_offer = item_info["special_offer"]
            free_item = special_offer["free_item"]
            free_count = special_offer["free_count"]
            qualifying_sets = count // special_offer["requires"]

            # Record the free items to be deducted later
            free_items[free_item] = free_items.get(free_item, 0) + qualifying_sets * free_count

        # Apply multi-buy offers
        if "offers" in item_info:
            for offer_quantity, offer_price in sorted(item_info["offers"], key=lambda x: -x[0]):
                total_price += (count // offer_quantity) * offer_price
                count %= offer_quantity

        # Add remaining items at regular price
        total_price += count * item_price

    # Deduct free items from total
    for free_item, free_count in free_items.items():
        if free_item in item_counts:
            # Determine how many free items can actually be deducted
            deducted_count = min(item_counts[free_item], free_count)
            item_counts[free_item] -= deducted_count
            total_price -= deducted_count * price_table[free_item]["price"]

    return total_price

