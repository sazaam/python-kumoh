from binarySearchTree import *
from functools import partial


def lookaround(n:TreeNode, char=""):
    print(char + str(n.item))
    if n.right :
        lookaround(n.right, "<")
    if n.left :
        lookaround(n.left, ">")




# 1. 첨부의 tree.png (10장 강의자료 23페이지 왼쪽 그래프) 모양대로 트리 만들기
T = BinarySearchTree()
T.insert(20)
T.insert(40)
T.insert(55)
T.insert(70)
T.insert(10)
T.insert(17)
T.insert(7)


lookaround(T.top())

'''
    20
    <40
    <55
    <70
    >10
    <17
    >7
'''

# 2. 루트노드 삭제
T.delete(20)

# 3. 40을 검색 후 40의 왼쪽노드 값과 오른쪽 노드 값 출력 (17, 55가 나와야 됨)
a = T.search(40)
print(a.left.item)
print(a.right.item)





