# noinspection PyUnusedLocal
def fizz_buzz(number):
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")

    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"
    else:
        return str(number)

