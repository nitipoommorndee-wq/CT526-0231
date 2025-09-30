# mylib.py

def myfunc(a, b):
    """
    Repeat string a, b times.
    Example:
        myfunc("x", 4) -> "xxxx"
    """
    a = str(a)
    try:
        n = int(b)
    except (ValueError, TypeError):
        raise ValueError("b must be an integer")

    if n < 0:
        raise ValueError("b must be non-negative")

    return a * n
