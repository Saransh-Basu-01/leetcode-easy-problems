class Solution:
    def isPalindrome(self, x):
        str_x = str(x)
        if str_x == str_x[::-1]:
            return True
        else:
            return False
s=Solution()
w=s.isPalindrome(121)
print(w)
a=s.isPalindrome(10)
print(a)