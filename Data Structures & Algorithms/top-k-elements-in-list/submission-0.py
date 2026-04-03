class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """

        note: itrating through hash is o(nlogn) due to the need to sort hash first 

        create hash
        
        add freq to hash

        create result array


        for i in range(k)
        """

        # track number frequences
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1

        # sort 
        sorted_by_value = dict(sorted(freq.items(), key=lambda item: item[1], reverse=True))

        # pick top k elements
        top_k = []
        keys = list(sorted_by_value.keys())
        for i in range(k):
            top_k.append(keys[i])

        return top_k
