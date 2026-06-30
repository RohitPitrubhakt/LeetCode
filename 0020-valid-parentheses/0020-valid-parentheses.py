class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')':'(',']':'[','}':'{'}
        comp = []
        for i in s:
            if i in brackets:
                if not(comp) or comp.pop() != brackets[i]:
                    return False
            else:
                comp.append(i)
        return len(comp) == 0