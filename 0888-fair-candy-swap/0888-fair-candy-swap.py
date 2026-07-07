class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        for val in aliceSizes:
            res = val - diff
            if res in bobSizes:
                return [val , res]