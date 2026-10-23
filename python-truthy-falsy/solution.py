def is_truthy(value) -> bool:
    """
    Return the truthiness of `value` exactly as Python's own
    rules would determine it (equivalent to bool(value), but
    implement the logic explicitly rather than calling bool()
    directly, handle None, numbers, strings, lists, tuples,
    dicts, and sets).
    """
    if value is None or value is False:
        return False
    if value is True:
        return True
    
    # Check for zero in numeric types
    if isinstance(value, (int, float, complex)):
        return value != 0
        
    # Check for empty sequences and collections
    if isinstance(value, (str, list, tuple, dict, set)):
        return len(value) > 0
        
    # Default fallback for custom objects
    return True


def first_truthy(values: list):
    """
    Return the first value in `values` that is truthy. If no
    value in the list is truthy, return None.
    Do not use Python's built-in `any()`, implement the scan
    explicitly using is_truthy-style checks.
    """
    for value in values:
        if is_truthy(value):
            return value
            
    return None
