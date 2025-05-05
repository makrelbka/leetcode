class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        arr = {}
        l = 0
        r = 0
        max_len = 0
        len_s = len(s)

        while r < len_s:
            val = s[r]
            if val in arr and arr[val] >= l:
                l = arr[val] + 1
            else:
                max_len = max(max_len, r - l + 1)
            
            arr[val] = r
            r += 1
        
        return max_len


"""
Longest Substring Without Repeating Characters
Идем по строчке двумя указателями 
Используем мапу для хранения индексов символов и проверки на наличие символов
Если, встретили символ,который уже был после левой границы то двигаем левую границу 
Иначе, обновляем максимальную длину
"""