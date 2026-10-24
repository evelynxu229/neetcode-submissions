class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numbers = set(nums)
        max_length = 0

        for i in numbers:
            if i+1 in numbers:
                continue
            else:
                length=1
                start = i-1
                while start in numbers:
                    start-=1
                    length+=1
                if length>max_length:
                    max_length = length
        return max_length



            




