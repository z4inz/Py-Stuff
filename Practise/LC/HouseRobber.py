class Solution:
    def rob(self, nums: List[int]) -> int:
        #Array looks like [n1, n2, nums[0], nums[1], nums[2], etc...]
        n1 = 0
        n2 = 0
        for i in range(len(nums)):
            res = max(n1 + nums[i], n2) #Because can't rob adjacents, find max of current + 2 before, and 1 before
            n1 = n2 #Set n1 as what comes next (n2)
            n2 = res #n2 is value just found
        return res
