"""Ex07 - Dictionary Functions."""
__author__ = "730394136"


def invert(inp_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values."""
    out_dict: dict[str, str] = {}
    for key in inp_dict:
        if inp_dict[key] in out_dict:
            raise KeyError("More than one of the same key.")
        out_dict[inp_dict[key]] = key
    return out_dict 


def favorite_color(colors: dict[str, str]) -> str:
    """Returns the color that appears most frequently."""
    fav_color: str = ""
    new_dict: dict[str, int] = {}
    for key in colors:
        if colors[key] in new_dict:
            new_dict[colors[key]] += 1
        else:
            new_dict[colors[key]] = 1
    i: int = 0
    for key in new_dict:
        if new_dict[key] > i:
            i = new_dict[key]
            fav_color = key
    return fav_color


def count(inp_list: list[str]) -> dict[str, int]:
    """Counts amount of times a value appeared in input list."""
    out_dict: dict[str, int] = {}
    for elem in inp_list:
        if elem in out_dict:
            out_dict[elem] += 1 
        else:
            out_dict[elem] = 1
    return out_dict