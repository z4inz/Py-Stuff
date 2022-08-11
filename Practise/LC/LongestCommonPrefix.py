class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        if size == 0:
            return ""
        if size == 1:
            return strs[0]

        strs = sorted(strs)

        end = min(strs[0], strs[size-1])

        i = 0
        while (i < len(end) and strs[0][i] == strs[size-1][i]):
            i += 1
        return strs[0][:i]
