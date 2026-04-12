class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        seen = set()
        maxCount = 0
        start, end = 0, 0

        while end < len(s):
            # add not seen before character
            if s[end] not in seen:
                seen.add(s[end])
                end += 1

            # removed seen before character
            else:
                seen.remove(s[start])
                start += 1

            maxCount = max(maxCount, len(seen))

        return maxCount

            