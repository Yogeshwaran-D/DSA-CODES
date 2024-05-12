class Solution:
    def longestOnes(self, nums, k) :
        n=len(nums)
        low,high=0,0
        maxValue=0
        zero=0
        while high < n :
            if nums[high] == 0 :
                zero+=1
            while zero > k :
                if nums[low] == 0 :
                    zero-=1
                low+=1
            if zero<=k:
                maxValue=max(maxValue,high-low+1)
            high+=1
        return maxValue
