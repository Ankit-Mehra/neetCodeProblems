"""Given an integer array nums, return an array answer such that answer[i]
is equal to the product of all the elements of nums except nums[i].
"""

def product_except_self(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that 
    answer[i] is equal to the product of all the elements of nums except nums[i].
    """
    # Initialize an empty array to store the products
    products = [1] * len(nums)

    # Calculate the product of all elements in the input array
    # except for the element at the current index
    product = 1
    for i in range(len(nums)):
        products[i] = product
        product *= nums[i]

    # Reset the product and calculate the product of all elements
    # in the input array except for the element at the current index
    product = 1
    for i in reversed(range(len(nums))):
        products[i] *= product
        product *= nums[i]

    return products


def product_except_self2(nums: list[int]) -> list[int]:
    """Given an integer array nums, return an array answer such that 
    answer[i] is equal to the product of all the elements of nums except nums[i].
    """
    products = [1] * len(nums)
    i = 0
    while i < len(nums):
        product = 1
        for j in range(len(nums)):
            if i == j :
                product *= 1
            else:
                product *= nums[j]
        products[i] = product
        i += 1
    return products   

if __name__ == "__main__":
    nums = [1,2,3,4]
    print(product_except_self(nums))
