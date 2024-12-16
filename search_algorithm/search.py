
DATA_PATH = 'data.txt'

def simple_search(data: list, to_find: int) -> int | None:
    """data: list of int digit\n
    to_find: searching int value\n
    RETURNS: index of value if found and None if not"""
    res = list()
    for i in range(len(data)):
        if data[i] == to_find: res.append(i)

    return res if len(res) else None

def binary_search_all(data: list, to_find: int) -> list[int] | None:
    """data: SORTED list of int
    to_find: int"""

    min_index = 0
    max_index = len(data) - 1

    res = list()

    while min_index < max_index:
        mid = (max_index + min_index) // 2
            
        if to_find > data[mid]: min_index = mid + 1
        else: max_index = mid
    
    while min_index < len(data) and data[min_index] == to_find:
        res.append(min_index)
        min_index += 1
        
    return res if len(res) else None

def binary_search_one(data: list, to_find: int) -> int | None:
    """data: SORTED list of int
    to_find: int"""

    min_index = 0
    max_index = len(data) - 1

    while min_index < max_index:
        mid = (max_index + min_index) // 2
            
        if to_find > data[mid]: min_index = mid + 1
        else: max_index = mid
    
    if data[min_index] == to_find: return min_index



    

