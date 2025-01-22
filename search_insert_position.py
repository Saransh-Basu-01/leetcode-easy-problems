class Solution():
    def searchInsert(self,nums,target):
        low=0
        n=len(nums)
        high=n-1
        while (low<=high):
            # mid=low+(high-low)//2
            mid=(high+low)//2
            if(nums[mid]==target):
                return mid
            elif(nums[mid]>target): #search in the left half
                high=mid-1
            else:#search in the right half
                low=mid+1
        return low
    
s=Solution()
nums=[2,5,9,11,15,17,20,42]
target=23
print(s.searchInsert(nums,target))