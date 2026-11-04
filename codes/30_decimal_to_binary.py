"""Program 30: Convert decimal to binary without using bin()."""


def decimal_to_binary(number):
    """Return the binary digits of number as a string.

    - 0 returns "0".
    - A negative number raises ValueError.
    """
    if number < 0:
        raise ValueError("Negative numbers are not allowed")
    if number == 0:
        return "0"
    bits = ""
    while number > 0:
        bits = str(number % 2) + bits   # remainder goes in front
        number = number // 2
    return bits


if __name__ == "__main__":
    n = int(input("Enter a decimal number: "))
    print("Binary:", decimal_to_binary(n))
