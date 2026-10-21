class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic={}

        for i in nums:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
        
        sorted_nums = sorted(dic, key=dic.get, reverse=True)
        return sorted_nums[:k]