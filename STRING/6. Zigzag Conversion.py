class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 : return s
        res=""
        n=len(s)
        incrementer= 2 * (numRows-1)
        for r in range(numRows):
            for i in range(r,n,incrementer):
                res+=s[i]
                if r > 0 and r < numRows-1 and  (i + incrementer) - (2 * r) < n:
                    res+=s[(i + incrementer) - (2 * r)]
        return res  