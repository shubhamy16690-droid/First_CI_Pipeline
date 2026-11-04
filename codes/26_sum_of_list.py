"""Program 26: Sum of the elements of a list without using sum()."""


def sum_of_list(numbers):
    """Return the sum of all elements. An empty list gives 0."""
    total = 0
    for n in numbers:
        total += n
    return total


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Sum:", sum_of_list(data))
