def containsDuplicate(nums: list) -> bool:
    if len(nums) <= 1:
        return False
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j]:
                return True
    return False

def containsDuplicate2(nums: list) -> bool:
  ref = {}
  for num in nums:
    if num not in ref:
      ref[num] = 1
    else:
      return True
  return False


def countDuplicate(nums:list)->bool:
  ref = {}
  for num in nums:
    if num in ref:
      ref[num] += 1
    else:
      ref[num] = 1
  return ref


def main():
    print(containsDuplicate2([1, 2, 3, 4]))
    print(countDuplicate([1, 2, 3, 3, 2, 4,4]))


if __name__ == "__main__":
    main()
