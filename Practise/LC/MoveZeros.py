class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        x = len(nums)
        current = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[current] = nums[i]
            else:
                continue
            current += 1
        diff = x - current
        for i in range(1, diff + 1):
            nums[-i] = 0
