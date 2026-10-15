class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_s = {}
        dic_t = {}
        for a in s:
            if a not in dic_s:
                dic_s[a]=1
            else:
                dic_s[a]+=1

        for a in t:
            if a not in dic_t:
                dic_t[a]=1
            else:
                dic_t[a]+=1
        
        return dic_s==dic_t
        
        