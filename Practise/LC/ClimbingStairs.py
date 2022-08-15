class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        n1 = 0
        n2 = 1
        temp = 0
        for i in range(n):
            temp = n1 + n2
            n1 = n2
            n2 = temp
        return temp
