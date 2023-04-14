import string


def to_kebab_case(s: str) -> str:
    """
    Convert a string to kebab case, removing all punctuation.
    """
    # Remove all punctuation from the string
    s = s.translate(str.maketrans("", "", string.punctuation))

    # Split the string into words, convert to lowercase, and join with hyphens
    words = s.split()
    return "-".join(word.lower() for word in words)
