# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def sym(a, b):
    if a == None and b == None:
        return True
    if a == None or b == None:
        return False
    cond = a.val == b.val
    l = sym(a.left, b.right)
    r = sym(b.left, a.right)
    return cond and l and r

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return sym(root.left, root.right)


"""
Symmetric Tree
Идем по дереву
Берем левое и правое и отправляем в функцию, 
В функции проверяем на то что вершины симметричны если мы внизу, иначе запускаем дальше для детей и сравнниваем значения в которые уже пришли
"""