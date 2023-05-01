"""Given an array of integers nums and an integer target,
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order."""


def twoSum(nums: list[int], target: int) -> list[int]:
    """This solution takes O(n^2) time"""
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]

def twoSum3(nums: list[int], target: int) -> list[int]:
    """This  will also takes O(n^2) time"""
    for i, v in enumerate(nums): # more efficient than range(len(nums))
        for j in range(i+1,len(nums)):
            if v + nums[j] == target:
                return (i,j)

def twoSum2(nums: list[int], target: int) -> list[int]:
    """This will take O(n) time"""
    map_dic = {}
    for indx, num in enumerate(nums):
        diff = target - num
        if diff in map_dic:
            return [map_dic[diff], indx]
        map_dic[num] = indx
    return []

def main():
    """main function"""
    print(twoSum([2, 7, 11, 15], 9))
    print(twoSum2([2, 7, 11, 15], 9))
    print(twoSum([3, 2, 3], 6))
    print(twoSum2([3, 2, 3], 6))


if __name__ == "__main__":
    main()
