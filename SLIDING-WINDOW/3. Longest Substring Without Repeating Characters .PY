class Solution:
    def lengthOfLongestSubstring(self, s) :
        new_dict={}
        low=0
        maxSubString=0
        for high in range(len(s)):
            if new_dict.get(s[high]) != None:
                if new_dict.get(s[high]) >=low:
                    low=new_dict.get(s[high])+1
            maxSubString=max(maxSubString,high-low+1)
            new_dict[s[high]]=high
        return maxSubString