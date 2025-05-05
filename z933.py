class RecentCounter:

    def __init__(self):
        self.arr = []
        self.st = 0

    def ping(self, t: int) -> int:
        self.arr.append(t)
        while t - self.arr[self.st] > 3000:
            self.st += 1
        return len(self.arr) - self.st


"""
Number Of Recent Calls
Заводим массив и перерменную указывающую на начало списка 
Теперь при каждом добавлении элемента будем двигать старт до момента пока разница не станет меньше 3000
И выводим число элментов от старта до конца
"""