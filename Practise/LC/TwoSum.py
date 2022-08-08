class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict = {}
        for i in range(len(nums)):
            if not (target - nums[i] in dict):
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]
