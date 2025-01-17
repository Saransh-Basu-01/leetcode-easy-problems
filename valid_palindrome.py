class Solution():
    def isPalindrome(self, s):
        filtered_chars=""
        for char in s:
            if char.isalnum():
                filtered_chars+=char.lower()
        return filtered_chars==filtered_chars[::-1] 
# string[::-1]:
# Start: No value provided, so it starts from the last character of the string.
# Stop: No value provided, so it continues to the first character.
# Step: -1, meaning move one step backward.
s=Solution()
print(s.isPalindrome("A man, a plan, a canal: Panama "))
print(s.isPalindrome("race a car"))