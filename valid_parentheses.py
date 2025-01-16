#solving using stack=FILO
class Solution():
    def isVaild(self,s):
        stack=[]
        for c in s:
            if c=='(':
                stack.append(')')
            elif c=='[':
                stack.append(']')
            elif c=='{':
                stack.append('}')
            else:
                if not stack or stack.pop()!=c:
                    return False 
        return not stack
    
s=Solution()
print(s.isVaild("[{()[]}()]"))
print(s.isVaild(")"))
            
                