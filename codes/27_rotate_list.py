"""Program 27: Rotate a list by k positions to the right."""


def rotate_list(items, k):
    """Return a NEW list rotated right by k positions.

    - k can be larger than the list length.
    - A negative k rotates to the left.
    - An empty list returns [].
    """
    if len(items) == 0:
        return []
    k = k % len(items)              # handles big and negative k
    if k == 0:
        return list(items)
    return items[-k:] + items[:-k]


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by space: ").split()]
    steps = int(input("Rotate by k: "))
    print("Rotated:", rotate_list(data, steps))
