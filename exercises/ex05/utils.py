"""EX05 - 'list' Utility Functions."""
__author__ = "730394136"

def only_evens(xs: list[int]) -> list[int]:
    """Returns even elements of input parameter."""
    number: list[int] = []
    for elem in xs:
        if elem % 2 == 0:
            number.append(elem)
    return number

def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Returns list containing all elements of the first and second lists."""
    number: list[int] = []
    for item in xs:
        number.append(item)
    for item in ys:
        number.append(item)
    return number

def sub(xs: list[int], ys: int, zs: int) -> list[int]:
    """Returns list as subset of the given list in range."""
    if ys < 0:
        ys = 0
    if zs > len(xs):
        zs = len(xs) 
    r_list: list[int] = []
    for idx in range(ys, zs):
        r_list.append(xs[idx])
    return r_list