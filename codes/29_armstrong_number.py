"""Program 29: Check whether a number is an Armstrong number."""


def is_armstrong(number):
    """Return True if the sum of digits^(number of digits) equals the number.

    Negative numbers return False.
    """
    if number < 0:
        return False
    digits = str(number)
    power = len(digits)
    total = 0
    for d in digits:
        total += int(d) ** power
    return total == number


if __name__ == "__main__":
    n = int(input("Enter a number: "))
    print("Armstrong" if is_armstrong(n) else "Not Armstrong")
