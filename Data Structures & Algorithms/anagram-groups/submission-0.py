class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic={}
        for item in strs:
            sort_str = "".join(sorted(item))

            if sort_str in dic:
                dic[sort_str].append(item)
            else:
                dic[sort_str]=[item]
        
        return list(dic.values())
