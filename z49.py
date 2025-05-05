class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for i in strs:
            result[''.join(sorted(i))].append(i)
        return list(result.values())
                    

"""
Group Anagrams
Идем по списку слов
В каждое слово сортируем чтобы использовать как ключ 
По полученному ключу кладем в мапу слово 
Тем самым слова состоящие из одних букв будут класться по одному ключу 
"""