class solution():
    def romantoint(self,s):
        roman_values={
            'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000
        }
        prev_value=0
        total=0
        for char in reversed(s):
            current_value=roman_values[char]
            if current_value<prev_value:
                total-=current_value
            else:
                total+=current_value
            prev_value=current_value
        return total
    
s=solution()
print(s.romantoint("IX"))
print(s.romantoint("MCMXCIV"))