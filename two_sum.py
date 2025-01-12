def twoSum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i
nums=[2,7,11,14]
target=13
result=twoSum(nums,target)
print(result)
#using class we arenot using self. in this class because we dont need to have instance attribute
class Solution:
    def twoSum(self, nums, target):
        num_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_dict:
                return [num_dict[complement], i]
            num_dict[num] = i
solution = Solution()
nums = [2, 7, 11, 15]
target = 9
result = solution.twoSum(nums, target)
print("Indices of numbers that add up to the target are:", result)
