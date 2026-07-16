class Solution:
    def isValid(self, s: str) -> bool:

        pairs = {
             ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for ch in s:
            if ch in "({[":
                stack.append(ch)
