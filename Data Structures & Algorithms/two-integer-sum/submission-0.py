class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dic={}
        for i in range(0, len(nums)):
            nums_dic[nums[i]]=i

        for i in range(0, len(nums)):
            complement = target-nums[i]
            if (complement in nums_dic) and (nums_dic[complement] != i):
                return [i,nums_dic[complement]]