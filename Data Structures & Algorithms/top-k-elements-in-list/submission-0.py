class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numdict = defaultdict(int)

        for i in nums:
            numdict[i] += 1

        sorted_nums = sorted(numdict, key=numdict.get, reverse=True)

        return sorted_nums[:k]
