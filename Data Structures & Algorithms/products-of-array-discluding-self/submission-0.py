class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]


        for i in range(0, len(nums)):
            if i==0:
                prefix.append(1)
                continue
            
            prefix.append(nums[i-1]*prefix[i-1])

        n = len(nums)
        suffix = [1] * n

        for i in range(n-2, -1, -1):
            suffix[i]=nums[i+1] * suffix[i+1]
        
        answer=[_ for _ in range(0, len(nums))]

        for i in range(0, len(nums)):
            answer[i]=prefix[i]*suffix[i]
        
        return answer
        

