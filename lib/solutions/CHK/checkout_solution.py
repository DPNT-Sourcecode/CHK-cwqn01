def checkout(skus):
    # Price table and special offers
    price_table = {
        "A": {"price": 50, "offers": [(3, 130), (5, 200)]},
        "B": {"price": 30, "offers": [(2, 45)]},
        "C": {"price": 20},
        "D": {"price": 15},
        "E": {"price": 40, "special_offer": {"requires": 2, "free_item": "B", "free_count": 1}},
        "F": {"price": 10, "special_offer": {"requires": 3, "free_item": "F", "free_count": 1}},
        "G": {"price": 20},
        "H": {"price": 10, "offers": [(5, 45), (10, 80)]},
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
            if count >= special_offer["requires"]:
                qualifying_sets = count // special_offer["requires"]
                free_item = special_offer["free_item"]
                free_count = special_offer["free_count"]

                # Add free items to the free_items dictionary
                free_items[free_item] = free_items.get(free_item, 0) + qualifying_sets * free_count

    # Step 2: Calculate price for items and apply multi-buy offers
    for sku, count in item_counts.items():
        # Apply special offer first if free items are involved
        if sku in free_items:
            free_count = free_items[sku]
            count -= min(count, free_count)  # Deduct the free items

        # Apply multi-buy offers if available
        if "offers" in price_table[sku]:
            for offer_quantity, offer_price in sorted(price_table[sku]["offers"], key=lambda x: -x[0]):
                if count >= offer_quantity:
                    total_price += (count // offer_quantity) * offer_price
                    count %= offer_quantity  # Remaining items after offer

        # Add the remaining items at regular price
        total_price += count * price_table[sku]["price"]

    # Handle regular items without special offers (like G, H, I, etc.)
    for sku, count in item_counts.items():
        if "offers" not in price_table[sku]:  # For items without special offers
            total_price += count * price_table[sku]["price"]

    return total_price