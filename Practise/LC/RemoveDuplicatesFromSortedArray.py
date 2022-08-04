class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        current = nums[0]
        for i in range(len(nums)):
            if nums[i] == current:
                continue
            else:
                nums[count] = nums[i]
            count += 1
            current = nums[i]
        return count
