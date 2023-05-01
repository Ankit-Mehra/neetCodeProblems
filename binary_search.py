""" Binary Search Algorithm """
def binary_search(some_list:list,number:int) -> int:
    """given a sorted list provide the index of matching number"""
    start = 0
    end = len(some_list)

    while end > start:
        mid = (start + end)//2
        pivot = some_list[mid]
        if pivot == number:
            return mid
        if pivot < number:
            start = mid
        else:
            end = mid
    return None

def binary_search_recursive(some_list:list,number:int) -> int:
    """given a sorted list provide the index of matching number"""
    start = 0
    end = len(some_list)
    mid = (start + end)//2
    pivot = some_list[mid]
    if pivot ==  number :
        return mid
    if pivot < number:
        return mid + binary_search_recursive(some_list[mid:],number)
    if pivot > number:
        return  binary_search_recursive(some_list[:mid],number)

if __name__ == "__main__":
    new_list = [9,10,11,12,45,89,100,156,158]
    print(binary_search(new_list,45))
    print(binary_search_recursive(new_list,12))
