class solution():
    def lengthOfLastWord(self,s):
        i=len(s)-1
        length=0
        while i>=0 and s[i]==" ":
            i-=1
        while i>=0 and s[i]!=" ":
            length=length+1
            i-=1
        return length
s=solution()
a="  fly me  to   moon  "
b="luffy is a joyboy"
print(s.lengthOfLastWord(a))
print(s.lengthOfLastWord(b))