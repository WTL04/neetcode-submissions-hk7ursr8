class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        seen = {}
        start, end = 0, 0
        replacements = k
        max_freq = 0
        max_length = 0
        

        for end in range(len(s)):
            # add or increment into seen hash
            char = s[end]
            seen[char] = 1 + seen.get(char, 0)
            max_freq = max(max_freq, seen[char])

            # find number of characters we have to replace
            window_length = (end - start + 1)
            characters_to_change = window_length - max_freq

            # if we need to replace more than our replacement budget, then the window is invalid
            if characters_to_change > replacements:
                # invalid window, shrink from start
                seen[s[start]] -= 1
                start += 1

                # recompute max freq
                max_freq = max(max_freq, seen[char])
            else:
                # update max_length only if the window is valid
                max_length = max(window_length, max_length)

        return max_length