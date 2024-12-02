
# noinspection PyUnusedLocal
# skus = unicode string
def checklite(skus):
    if not isinstance(skus, str):
        raise ValueError("Input must be a Unicode string.")

    if not skus.isalpha():
        raise ValueError("Input must contain only alphabetic characters.")

    return f"Validated input: {skus}"
