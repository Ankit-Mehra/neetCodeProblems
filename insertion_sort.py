"""Insertion sort function as coleman"""


def insertion_sort(nums: list) -> list:
    """insertion sort algorithm"""
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def insertion_sort_dec(nums: list) -> list:
    """insertion sort algorithm"""
    for i in range(1, len(nums)):
        key = nums[i]
        j = i - 1
        while j >= 0 and nums[j] < key:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    return nums


def insertion_sort2(nums: list) -> list:
    """insertion sort with first element as key"""
    i = 0
    while i < (len(nums) - 1):
        j = i + 1
        key = nums[j]
        while j >= 0 and i >= 0:
            if nums[i] > key:
                nums[i + 1] = nums[i]
                i -= 1
                j -= 1
            else:
                break
                # i += 1
        nums[j] = key
        i += 1
    return nums


def insertion_sort3(nums: list) -> list:
    """insertion sort where ewe find the lowest no. and
    place it in first position"""
    for i in range(len(nums)):
        smallest = i
        j = i+1
        while j < len(nums): 
            if nums[j] < nums[smallest]:
                smallest = j
            j+=1
        least_no = nums[smallest]
        nums[smallest] = nums[i]
        nums[i] = least_no
    return nums


print(insertion_sort3([5, 2, 4, 6, 1, 3]))
print(insertion_sort_dec([5, 2, 4, 6, 1, 3]))

