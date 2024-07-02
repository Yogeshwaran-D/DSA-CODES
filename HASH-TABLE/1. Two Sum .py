class Solution:
    def twoSum(self, nums, target):
        temp={}
        for i in range(len(nums)):
            if temp.get((target-nums[i])) is not None:
                return [temp.get(target-nums[i]),i]
            temp[nums[i]]=i