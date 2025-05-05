from typing import List


class Solution:
    def compress(self, chars: List[str]) -> int:
        pos = 0
        cnt = 1
        
        for i in range(1, len(chars) + 1): 
            if i < len(chars) and chars[i] == chars[i - 1]:
                cnt += 1
            else:
                chars[pos] = chars[i - 1]
                pos += 1
                if cnt > 1:
                    for d in str(cnt):
                        chars[pos] = d
                        pos += 1
                cnt = 1
        
        return pos

s = Solution()
print(s.compress(["a","a","b","b","c","c","c"]))
print(s.compress(["a"]))
print(s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))

"""
String Compression

Будем идти по массиву
Если будет встречать тот же символ что и предыдущий то увеличиваем счетчик
Иначе будем записывать в результат предыдущий символ и счетчик (если он больше 1)(записываем через for так как каждый элемент должен быть числом), и обнулять счетчик 
"""