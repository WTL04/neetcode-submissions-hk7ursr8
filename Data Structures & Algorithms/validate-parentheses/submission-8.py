class Solution:
    def isValid(self, s: str) -> bool:
        # edge case: no string or odd number string
        if len(s) == 0 or len(s) % 2 != 0:
            return False

        mapping = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        stack = []

        for c in s:

            # check for opening brackets
            if c not in mapping: 
                stack.append(c)

            # check for closing brackets
            else:

                # if empty stack or no matching opening bracket at top of stack, return false
                if not stack or stack[-1] != mapping[c]:
                    return False

                # else remove valid pair
                stack.pop()


        return len(stack) == 0