def checkout(skus):
    # Price table and offers (simplified representation using dictionaries)
    price_table = {
        "A": {"price": 50, "offers": [(3, 130), (5, 200)]},
        "B": {"price": 30, "offers": [(2, 45)]},
        "C": {"price": 20},  # No offers
        "D": {"price": 15},  # No offers
        "E": {"price": 40, "special_offer": {"requires": 2, "free_item": "B", "free_count": 1}},
        "F": {"price": 10, "special_offer": {"requires": 3, "free_item": "F", "free_count": 1}},
        "G": {"price": 20},  # No offers
        "H": {"price": 10, "offers": [(5, 45), (10, 80)]},
        "I": {"price": 35},  # No offers
        "J": {"price": 60},  # No offers
        "K": {"price": 80, "offers": [(2, 150)]},
        "L": {"price": 90},  # No offers
        "M": {"price": 15},  # No offers
        "N": {"price": 40, "special_offer": {"requires": 3, "free_item": "M", "free_count": 1}},
        "O": {"price": 10},  # No offers
        "P": {"price": 50, "offers": [(5, 200)]},
        "Q": {"price": 30, "offers": [(3, 80)]},
        "R": {"price": 50, "special_offer": {"requires": 3, "free_item": "Q", "free_count": 1}},
        "S": {"price": 30},  # No offers
        "T": {"price": 20},  # No offers
        "U": {"price": 40, "special_offer": {"requires": 4, "free_item": "U", "free_count": 1}},
        "V": {"price": 50, "offers": [(3, 130), (2, 90)]},
        "W": {"price": 20},  # No offers
        "X": {"price": 90},  # No offers
        "Y": {"price": 10},  # No offers
        "Z": {"price": 50},  # No offers
    }

    # If basket is empty, return 0
    if skus == "":
        return 0

    # Count occurrences of each SKU
    item_counts = {}
    for sku in skus:
        if sku not in price_table:
            return -1  # Return -1 for invalid SKU
        item_counts[sku] = item_counts.get(sku, 0) + 1

    total_price = 0
    free_items = {}

    # Step 1: Handle special offers (e.g., "2E get one B free", "3N get one M free")
    for sku, count in item_counts.items():
        if sku in price_table and "special_offer" in price_table[sku]:
            special_offer = price_table[sku]["special_offer"]
            if count >= special_offer["requires"]:
                qualifying_sets = count // special_offer["requires"]
                free_item = special_offer["free_item"]
                free_count = special_offer["free_count"]

                # Add free items to the free_items dictionary
                free_items[free_item] = free_items.get(free_item, 0) + qualifying_sets * free_count

    # Step 2: Calculate price for items and apply multi-buy offers or just the price if no offers
    for sku, count in item_counts.items():
        # If there are free items, reduce the count
        if sku in free_items:
            free_count = free_items[sku]
            count -= min(count, free_count)  # Deduct the free items

        # Handle items with offers (multi-buy offers)
        if "offers" in price_table[sku]:
            for offer_quantity, offer_price in sorted(price_table[sku]["offers"], key=lambda x: -x[0]):
                if count >= offer_quantity:
                    total_price += (count // offer_quantity) * offer_price
                    count %= offer_quantity  # Remaining items after offer

        # Add the remaining items at regular price
        total_price += count * price_table[sku]["price"]

        # If no offers apply, simply add the regular price (items without "offers" or "special_offer")
        if "offers" not in price_table[sku] and "special_offer" not in price_table[sku]:
            print(count)
            print(price_table[sku]["price"])
            total_price += (count - 1 )* price_table[sku]["price"]

    return total_price








