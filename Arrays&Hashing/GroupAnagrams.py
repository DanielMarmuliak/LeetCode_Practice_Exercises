# Level: medium
class Solution(object):
    def groupAnagrams(self, strs):
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            if key in groups:
                groups[key].append(s)
            else:
                groups[key] = [s]
        result = list(groups.values())
        return result
