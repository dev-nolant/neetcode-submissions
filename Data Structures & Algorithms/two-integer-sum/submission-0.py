class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        return [
            [i, j]
            for i, x in enumerate(nums)
            for j, y in enumerate(nums)
            if x + y == target and i < j
            ][0]