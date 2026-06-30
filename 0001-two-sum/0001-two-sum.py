class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        dt = {}
        for x in nums:
            if target - x in dt:
                return [dt[target - x],i]
            else:
                dt[x]=i
            i += 1