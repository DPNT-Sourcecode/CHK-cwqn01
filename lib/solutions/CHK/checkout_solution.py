def checkout(skus):
    """
    Calculates the total cost of a basket of items based on the provided special offers.

    Args:
        skus (str): A string containing the stock-keeping units (SKUs) of the items in the basket.

    Returns:
        int: The total cost of the basket, or -1 if the input contains any illegal items.
    """
    # Split the input string into individual items
    item_list = list(skus)

    # Initialize the total cost to 0
    total_cost = 0

    # Initialize counters for each item
    item_count = [0] * 26

    # Count the occurrences of each item
    for item in item_list:
        index = ord(item) - ord('A')
        if index < 0 or index >= 26:
            return -1  # Illegal item
        item_count[index] += 1

    # Calculate the total cost
    for i, count in enumerate(item_count):
        if count > 0:
            item = chr(i + ord('A'))
            total_cost += get_offer_price(item, count)

    return total_cost


def get_offer_price(item, count):
    """
    Calculates the cost of an item based on the provided special offers.

    Args:
        item (str): The stock-keeping unit (SKU) of the item.
        count (int): The number of the item in the basket.

    Returns:
        int: The total cost of the item after applying any special offers.
    """
    price_table = {
        'A': (50, 130, 200),
        'B': (30, 45, 0),
        'C': (20, 0, 0),
        'D': (15, 0, 0),
        'E': (40, 0, 40),
        'F': (10, 10, 0),
        'G': (20, 0, 0),
        'H': (10, 45, 80),
        'I': (35, 0, 0),
        'J': (60, 0, 0),
        'K': (80, 150, 0),
        'L': (90, 0, 0),
        'M': (15, 0, 15),
        'N': (40, 40, 0),
        'O': (10, 0, 0),
        'P': (50, 200, 0),
        'Q': (30, 80, 0),
        'R': (50, 50, 0),
        'S': (30, 0, 0),
        'T': (20, 0, 0),
        'U': (40, 40, 0),
        'V': (50, 90, 130),
        'W': (20, 0, 0),
        'X': (90, 0, 0),
        'Y': (10, 0, 0),
        'Z': (50, 0, 0)
    }

    price, offer1, offer2 = price_table[item]

    if offer1 > 0 and count >= 3:
        full_offers = count // 3
        remainder = count % 3
        return full_offers * offer1 + remainder * price
    elif offer2 > 0 and count >= 5:
        full_offers = count // 5
        remainder = count % 5
        return full_offers * offer2 + remainder * price
    else:
        return count * price
