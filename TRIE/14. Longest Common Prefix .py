class Solution:
    def longestCommonPrefix(self, strs):
        res=""
        strs.sort()
        for i in range(len(strs[0])):
            if strs[0][i] == strs[-1][i]:
                res+= strs[0][i]
            else:
                return res
        return res