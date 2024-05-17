class Solution:
    def characterReplacement(self, s, k):
        l,r,MaxLen,MaxFre=0,0,0,0
        new_dict={}
        while r < len(s):
            new_dict[s[r]]=1+new_dict.get(s[r],0)
            MaxFre=max(MaxFre,new_dict.get(s[r]))
            if (r-l+1)-MaxFre > k:
                new_dict[s[l]]-=1
                MaxFre=0
                l+=1
            if (r-l+1)-MaxFre <= k:
                MaxLen=max(MaxLen,(r-l+1))
            r+=1
        return MaxLen