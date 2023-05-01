"""Merge- Sort algorithm"""


import string


def merge_sort(arr: list) -> list:
    """Sort a given list"""
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sorted(left, right, arr)
    
def merge_sort_dict(arr: list, key:string, descending = True) -> list:
    """Sort a given list"""
    if len(arr) <= 1:
        return

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort_dict(left,key)
    merge_sort_dict(right,key)

    merge_sorted_dict(left, right, arr, key)


def merge_sorted(a: list, b: list, arr: list) -> list:
    """Merge two sorted list into a single sorted list"""
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a or j < len_b:
        if j >= len_b:
            arr[k] = a[i]
            i += 1
            k += 1
            continue
        if i >= len_a:
            arr[k] = b[j]
            j += 1
            k += 1
            continue

        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1

def extend(len_a,lenb):
    pass
        
def merge_sorted_dict(a: list, b: list, arr: list,key:string) -> list:
    """Merge two sorted list into a single sorted list"""
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a or j < len_b:
        if j >= len_b:
            arr[k] = a[i]
            i += 1
            k += 1
            continue
        if i >= len_a:
            arr[k] = b[j]
            j += 1
            k += 1
            continue

        if a[i][key] <= b[j][key]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1     
        
        

if __name__ == "__main__":
    a = [5, 6, 10, 56, 80]
    b = [1, 7, 11, 60, 90, 100]

    # print(merge_sorted(a, b))

    # arr = [45, 12, 7, 9, 54, 14, 59, 98, 18]
    # merge_sort(arr)
    # print(arr)

    elements = [
        { 'name': 'vedanth',   'age': 17, 'time_hours': 1},
        { 'name': 'rajab', 'age': 12,  'time_hours': 3},
        { 'name': 'vignesh',  'age': 21,  'time_hours': 2.5},
        { 'name': 'chinmay',  'age': 24,  'time_hours': 1.5},
    ]
    
    merge_sort_dict(elements,'time_hours')
    print(elements)
    print("==========")
    merge_sort_dict(elements,'name')
    print(elements)
