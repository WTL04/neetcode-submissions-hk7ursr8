class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if s and t are not the same length, return false
        # use hash to check s freq
        # use hash to check t freq
        # return if s == t


        if len(s) != len(t):
            return False

        s_hash = {}
        for c in s:
            if c not in s_hash:
                s_hash[c] = 1
            else:
                s_hash[c] += 1

 
        t_hash = {}
        for c in t:
            if c not in t_hash:
                t_hash[c] = 1
            else:
                t_hash[c] += 1

        return s_hash == t_hash        



