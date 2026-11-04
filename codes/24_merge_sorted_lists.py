"""Program 24: Merge two already sorted lists into one sorted list."""


def merge_sorted_lists(list1, list2):
    """Return one sorted list containing all elements of both lists."""
    merged = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    merged.extend(list1[i:])        # leftover elements of list1
    merged.extend(list2[j:])        # leftover elements of list2
    return merged


if __name__ == "__main__":
    a = [int(x) for x in input("Sorted list 1: ").split()]
    b = [int(x) for x in input("Sorted list 2: ").split()]
    print("Merged:", merge_sorted_lists(a, b))
