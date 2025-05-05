import random

class RandomizedSet:

    def __init__(self):
        self.arr = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        self.map[val] = len(self.arr)
        self.arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map:
            return False
        index = self.map[val]
        last_val = self.arr[-1]

        self.arr[index] = last_val
        self.map[last_val] = index

        self.arr.pop()
        del self.map[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.arr)


o = RandomizedSet()
o.insert(10)
o.insert(20)
o.remove(10)
print(o.getRandom())


"""
Insert Delete GetRandom O(1)
Заводим массив для значений и мапу значения в индекс массива 
По мапе проверяем наличие и получаем индекс 
По массиву получаем рандомный элемент
Вставляем элемент просто через ключ в мапу и в конце массива 
А удаляем из массива и мапы таим образом:
Убираем ненужный элемент в конец массива и мапы и затем удаляем 
А на его место ставим последний, тем самым не сбиваем индексы
"""