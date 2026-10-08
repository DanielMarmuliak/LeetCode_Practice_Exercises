class Solution(object):
    def topKFrequent(self, nums, k):
        dic = {}
        result = []
        for i in nums:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for _ in range(k):
            best_value = 0
            best_key = None
            for key, value in dic.items():
                if value > best_value:
                    best_value = value
                    best_key = key
            result.append(best_key)
            dic.pop(best_key)
        return result


if __name__ == "__main__":
    sol = Solution()
    print(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2))
    # print(sol.topKFrequent([1], 1))
    # print(sol.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2))
