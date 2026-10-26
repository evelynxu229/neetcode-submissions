class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer=[]
        sorted_nums=sorted(nums)

        for i in range(0, len(sorted_nums)-2):
            if i>0 and sorted_nums[i-1]==sorted_nums[i]:
                continue
            left_pointer = i+1
            right_pointer = len(sorted_nums)-1
            while left_pointer<right_pointer:
                temp_sum=sorted_nums[i]+sorted_nums[left_pointer]+sorted_nums[right_pointer]
                if temp_sum==0:
                    answer.append([sorted_nums[i], sorted_nums[left_pointer], sorted_nums[right_pointer]])

                    while left_pointer<right_pointer and sorted_nums[left_pointer+1]==sorted_nums[left_pointer]:
                        left_pointer+=1
                    while right_pointer>left_pointer and sorted_nums[right_pointer-1]==sorted_nums[right_pointer]:
                        right_pointer-=1

                    left_pointer+=1
                    right_pointer-=1
                    
                elif temp_sum>0:
                    right_pointer-=1
                else:
                    left_pointer+=1
        
        return answer


                    