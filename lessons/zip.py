"""CQ04"""

def zip(xs:list[str], ys:list[int]) -> dict[str,int]:
    key_values: dict[str, int] = {}
    if len(xs) != len(ys):
        return key_values
    for elem in range(0,len(xs)):
        key_values[xs[elem]] = ys[elem]
    return key_values
