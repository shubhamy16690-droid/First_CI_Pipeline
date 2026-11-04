"""Program 25: Find the maximum and minimum in a list without max()/min()."""


def find_max_min(numbers):
    """Return a tuple (maximum, minimum). Raise ValueError for an empty list."""
    if len(numbers) == 0:
        raise ValueError("List is empty")
    maximum = numbers[0]
    minimum = numbers[0]
    for n in numbers:
        if n > maximum:
            maximum = n
        if n < minimum:
            minimum = n
    return (maximum, minimum)


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Max, Min:", find_max_min(data))
