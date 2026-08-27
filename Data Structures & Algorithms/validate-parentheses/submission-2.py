class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        open_brackets = set(['(', '{', '['])
        close_to_open = {')':'(', '}':'{', ']':'['}

        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                if not stack:
                    return False

                if stack[-1] == close_to_open[c]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
