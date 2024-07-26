class Solution:
    def countSubstrings(self, s):
        def palindrome(l,r,s):
            res=0
            while l>=0 and r<len(s) and s[l] == s[r]:
                res+=1
                l-=1
                r+=1
            return res
        res=0
        for i in range(len(s)):
            res+=palindrome(i,i,s)
            res+=palindrome(i,i+1,s)
        return res
