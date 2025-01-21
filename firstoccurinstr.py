class solution():
    def str(self,haystack,needle):
        n=len(haystack)
        m=len(needle)
        if m==0:
            return 0
        for i in range (n-m+1):
            if haystack[i:i+m]==needle:
                return i
            
        return -1
s=solution()
haystack="sadbutsad"
needle="sad"
print(s.str(haystack,needle))
print(s.str("hello","world"))