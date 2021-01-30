import json
import string

def is_empty(data):
    """
    Evaluates data to see if it is empty (None, empty string, or empty dict).
    :param any data: The data to evaluate.
    :return: True if the data is empty, False otherwise.
    :rtype: bool
    """
    if isinstance(data, dict):
        return False if data else True
    return bool(data is None or data is "")

def is_not_empty(data):
    """
    Evaluates data to see if it is not empty (None or empty string).
    :param any data: The data to evaluate.
    :return: True if the data is not empty, False otherwise.
    :rtype: bool
     """
    return not is_empty(data)