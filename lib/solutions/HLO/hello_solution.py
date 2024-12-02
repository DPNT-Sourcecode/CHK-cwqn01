

# noinspection PyUnusedLocal
# friend_name = unicode string
def hello(friend_name):
    if not isinstance(friend_name, str):
        raise ValueError("Input must be a string.")
    if not friend_name.isalpha():
        raise ValueError("Input must contain only alphabetic characters (including Unicode letters).")

    return f"Hello, {friend_name}!"

