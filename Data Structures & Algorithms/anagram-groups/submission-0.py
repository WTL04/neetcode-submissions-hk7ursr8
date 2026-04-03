class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # edge case: 1 string
        if len(strs) == 1:
            return [strs]


        result = defaultdict(list) # key: unique char count, value: anagrams with same char count

        for s in strs:

            # use an array to track the freq of characters
            # reset every string
            count = [0] * 26 # a-z

            for c in s:
                count[ord(c) - ord("a")] += 1 # increment index of count 

                # a = 0 -> 0 - 0 = 0
                # b = 1 -> 1 - 0 = 1

            result[tuple(count)].append(s)

        return list(result.values())