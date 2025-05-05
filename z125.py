class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        while left < right:
            if not (s[left].isalpha() or s[left].isnumeric()):
                left += 1
                continue
            if not (s[right].isalpha() or s[right].isnumeric()):
                right -= 1
                continue
            if s[left].lower() != s[right].lower():
                return False
            right -= 1
            left += 1
        return True
    
"""
Valide Palindrome
идем двумя указателями от начала и конца строки
если символ не буква или цифра то пропускаем его
если символы не равны то возвращаем False
если все символы равны то возвращаем True
"""
