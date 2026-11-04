"""Program 22: Check whether two strings are anagrams."""


def is_anagram(first, second):
    """Return True if both strings use the same letters.

    Upper/lower case and spaces are ignored.
    """
    a = first.replace(" ", "").lower()
    b = second.replace(" ", "").lower()
    return sorted(a) == sorted(b)


if __name__ == "__main__":
    s1 = input("Enter first string: ")
    s2 = input("Enter second string: ")
    print("Anagram" if is_anagram(s1, s2) else "Not an anagram")
