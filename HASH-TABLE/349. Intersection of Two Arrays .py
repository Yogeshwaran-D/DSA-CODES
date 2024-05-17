class Solution:
    def intersection(self, nums1, nums2) :
        new_dict={}
        ans=[]
        for i in nums1:
            new_dict[i]=1
        for j in nums2:
            if new_dict.get(j,0) == 1:
                new_dict[j]=0
                ans.append(j)
        return ans