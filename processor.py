def filter_data(data, key, value):
    """
    Filters a list of dictionaries based on a key-value condition.

    :param data: List of dictionaries to be filtered.
    :param key: The key in the dictionaries to filter on.
    :param value: The value to filter by.
    :return: Filtered list of dictionaries.
    """
    return [item for item in data if item.get(key) == value]

def sort_data(data, key, reverse=False):
    """
    Sorts a list of dictionaries based on a specified key.

    :param data: List of dictionaries to be sorted.
    :param key: The key in the dictionaries to sort on.
    :param reverse: If True, sort in descending order.
    :return: Sorted list of dictionaries.
    """
    return sorted(data, key=lambda item: item.get(key), reverse=reverse)
