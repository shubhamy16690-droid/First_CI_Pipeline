"""Program 23: Sort a list without using sort() or sorted() (Bubble Sort)."""


def bubble_sort(numbers):
    """Return a NEW list sorted in ascending order. Original is unchanged."""
    result = list(numbers)          # copy, so the original list is not changed
    n = len(result)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        if not swapped:             # already sorted, stop early
            break
    return result


if __name__ == "__main__":
    data = [int(x) for x in input("Enter numbers separated by space: ").split()]
    print("Sorted:", bubble_sort(data))
