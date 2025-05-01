class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if nums == []:
            return []
        prev = nums[0]
        st = nums[0]
        en = nums[0]
        arr = []
        for i in range(1, len(nums)):
            if nums[i] - 1 == prev:
                en = nums[i]
                prev = nums[i]
            else:
                if st < en:
                    arr.append(str(st) + "->" + str(en))
                else:
                    arr.append(str(st))
                st = nums[i]
                prev = nums[i]
        if st < en:
            arr.append(str(st) + "->" + str(en))
        else:
            arr.append(str(st))
  
        return arr
    
"""
Summary ranges
Идем по массиву и обновляем 3 переменные старт конец и предыдущий 
Если предыдущий отличется на 1 то обновляем конец, иначе записываем отрезок и обновлем начало
"""