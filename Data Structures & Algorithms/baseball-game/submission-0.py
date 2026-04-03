class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for c in operations:
            # add previous two scores
            if len(stack) >= 2 and c == "+":
                sum = stack[-1] + stack[-2]
                stack.append(sum)

            # duplicate top most score
            elif stack and c == "D":
                double = stack[-1] * 2
                stack.append(double)

            # remove top most score
            elif stack and c == "C":
                stack.pop()

            # add integer  
            else:
                stack.append(int(c))

        # return total in stack
        total = 0
        for c in stack:
            total += int(c)

        return total
                