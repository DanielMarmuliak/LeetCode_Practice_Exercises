class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False
        d1 = {}
        for c in s:
            d1[c] = d1.get(c, 0) + 1
        for c in t:
            if c in d1:
                d1[c] -= 1
                if d1[c] == 0:
                    del d1[c]
            else:
                return False
        return not d1
