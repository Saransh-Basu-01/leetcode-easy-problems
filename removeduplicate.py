class Solution():
    def removeDuplicate(self,nums):
        j=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[j]=nums[i]
                j+=1

        return j,nums[:j]
s=Solution()
nums=[0,1,1,1,1,0,2,2,0,1,2,3,3,0,1,4]
nums.sort()
print(s.removeDuplicate(nums))
