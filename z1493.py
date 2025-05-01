class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = True
        max_subarray_len = 0
        left = 0
        right = 0
        len_nums = len(nums)
        while True:
            if right >= len_nums:
                break
            if nums[right] == 1:
                right += 1
            elif zero:
                zero = False
                right += 1
            else:
                zero = True
                max_subarray_len = max(max_subarray_len, right - left - 1)
                while nums[left] != 0 and left < len_nums:
                    left += 1
                left += 1
        max_subarray_len = max(max_subarray_len, right - left - 1)   
        return max_subarray_len
    
"""
Longest Subarray of 1's After Deleting One Element 

Идем двумя указателями
Двигаем правый пока встречаем 1 или 0 при условие что 0 встречался 1 раз
Когда не можем двигать правый начинаем двигать левый пока не встретим 0, тем самым убрав встретившийся ноль и получив возможность двигатьь правый

"""
