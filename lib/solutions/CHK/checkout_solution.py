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
        "F": {"price": 10, "special_offer": {"requires": 3, "free_item": "F", "free_count": 1}},
        "G": {"price": 20},
        "H": {"price": 10, "offers": [(10, 80), (5, 45)]},
        "I": {"price": 35},
        "J": {"price": 60},
        "K": {"price": 80, "offers": [(2, 150)]},
        "L": {"price": 90},
        "M": {"price": 15},
        "N": {"price": 40, "special_offer": {"requires": 3, "free_item": "M", "free_count": 1}},
        "O": {"price": 10},
        "P": {"price": 50, "offers": [(5, 200)]},
        "Q": {"price": 30, "offers": [(3, 80)]},
        "R": {"price": 50, "special_offer": {"requires": 3, "free_item": "Q", "free_count": 1}},
        "S": {"price": 30},
        "T": {"price": 20},
        "U": {"price": 40, "special_offer": {"requires": 4, "free_item": "U", "free_count": 1}},
        "V": {"price": 50, "offers": [(3, 130), (2, 90)]},
        "W": {"price": 20},
        "X": {"price": 90},
        "Y": {"price": 10},
        "Z": {"price": 50},
    }

    # Validate input
    if not isinstance(skus, str):
        return -1  # Return -1 for illegal input
    if skus == "":
        return 0  # Empty input returns 0

    # Count occurrences of each SKU
    item_counts = {}
    for sku in skus:
        if sku not in price_table:
            return -1  # Return -1 for illegal SKUs
        item_counts[sku] = item_counts.get(sku, 0) + 1

    # Calculate total price
    total_price = 0
    free_items = {}

    # Step 1: Handle free item offers (e.g., "2E get one B free", "3N get one M free")
    for sku, count in item_counts.items():
        if sku in price_table and "special_offer" in price_table[sku]:
            special_offer = price_table[sku]["special_offer"]
            qualifying_sets = count // special_offer["requires"]
            free_item = special_offer["free_item"]
            free_count = special_offer["free_count"]

            # Add free items to the free_items dictionary
            free_items[free_item] = free_items.get(free_item, 0) + qualifying_sets * free_count

    # Step 2: Deduct free items and calculate prices for all SKUs
    for sku, count in item_counts.items():
        if sku in free_items:
            # Deduct free items from the count of the SKU
            free_count = free_items[sku]
            count -= min(count, free_count)

        # Apply multi-buy offers if available
        if "offers" in price_table[sku]:
            for offer_quantity, offer_price in sorted(price_table[sku]["offers"], key=lambda x: -x[0]):
                total_price += (count // offer_quantity) * offer_price
                count %= offer_quantity

        # Add remaining items at their regular price
        total_price += count * price_table[sku]["price"]

    # Step 3: Handle items with no special offers (like G, H, I)
    for sku, count in item_counts.items():
        # Handle regular items without special offers
        if sku not in price_table[sku].get("offers", []):
            total_price += count * price_table[sku]["price"]

    return total_price

