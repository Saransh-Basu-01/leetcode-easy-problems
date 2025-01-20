class Solution():
    def removeElement(self,nums,val):
        i=0
        for j in range(len(nums)):
            if nums[j]!=val:
                nums[i]=nums[j]
                i+=1
        return i,nums[:i]
s=Solution()
nums=[0,1,2,3,4,0,1,2,4,0,3,4]
val=3
print(s.removeElement(nums,val))
