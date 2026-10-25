class Solution:
    def isPalindrome(self, s: str) -> bool:

        new_l=[]

        for i in s:
            if i.isalnum():
                new_l.append(i.lower())

        new_s="".join(new_l)

        left_p=0
        right_p=len(new_s)-1

        while left_p<right_p:

            if new_s[left_p]!=new_s[right_p]:
                return False
            else:
                left_p+=1
                right_p-=1
        
        return True