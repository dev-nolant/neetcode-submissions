class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [1] * n

        left = 1
        i = 0

        while i < n:
            output[i] = left
            left *= nums[i]
            i += 1

        right = 1
        i = n - 1

        while i >= 0:
            output[i] *= right
            right *= nums[i]
            i -= 1
        return output