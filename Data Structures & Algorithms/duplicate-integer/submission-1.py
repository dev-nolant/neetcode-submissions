class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        uniq = [x for x in nums if x not in seen and not seen.add(x)]

        return len(uniq) != len(nums)