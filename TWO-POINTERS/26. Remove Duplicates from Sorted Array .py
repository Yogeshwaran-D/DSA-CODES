class Solution:
    def removeDuplicates(self, nums):
        n=len(nums)
        unique_index=0
        for index in range(0,n):
            if nums[unique_index] != nums[index]:
                unique_index+=1
                nums[unique_index]=nums[index]
        return unique_index+1