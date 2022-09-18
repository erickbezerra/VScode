def create_phone_number(n):
    """Create Phone Number in a specific format from an array of 10 integers

    Args:
        n (int): 10 integers between 0 and 9

    Returns:
        _type_: (085) 323-2423
    """
    # your code here
    return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)
