class Solution:
    def reverse(self, x: int) -> int:
        x = [x for x in str(x)]
        l = 0
        r = len(x)-1

        if x[0] == "-":
            l += 1
        while l < r:
            x[l], x[r] = x[r], x[l]
            l += 1
            r -= 1
        x = int("".join(x))
        if (x < -2**31 or x > 2**31 - 1):
            return 0
        return x
