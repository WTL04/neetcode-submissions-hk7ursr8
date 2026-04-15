class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        premuatation conditions: 
        - same length -> fixed window of length s1
        - same letters and frequency -> hash
        """

        window_freq = defaultdict()
        s1_freq = defaultdict()
        start = 0
        k = len(s1)

        # preload s1 dict all character frequencies
        for char in s1:
            s1_freq[char] = 1 + s1_freq.get(char, 0)
        

        for end in range(len(s2)):
            # add all character freq from the window
            window_freq[s2[end]] = 1 + window_freq.get(s2[end], 0)

            # check if permutation exists
            if window_freq == s1_freq:
                return True

            if end - start + 1 == k: # shrink window when window exceeds size of s1
                window_freq[s2[start]] -= 1

                # if character freq is 0, remove from dict
                if window_freq[s2[start]] == 0:
                    del window_freq[s2[start]]

                start += 1

        return False




