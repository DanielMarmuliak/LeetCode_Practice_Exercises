class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []

        for i in range(len(nums)):
            result = 1
            for j in range(len(nums)):
                if j == i:
                    j += 1
                else:
                    result *= nums[j]
                    j += 1
            answer.append(result)
        return answer


if __name__ == "__main__":
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
