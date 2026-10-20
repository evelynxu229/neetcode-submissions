class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic={}
        for i in range(0, len(nums)):
            complement = target - nums[i]
            
            if complement in nums_dic:
                return [nums_dic[complement], i]
           
            nums_dic[nums[i]]=i


        