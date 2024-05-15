class Solution:
    def returnToBoundaryCount(self, nums):
        count,TotalSum=0,0
        for i in nums :
            TotalSum+=i
            if TotalSum == 0 :
                count+=1
        return count