class Heap:
	def __init__(self, *args):
		if len(args) != 0:
			self.__A = args[0] # 파라미터로 온 리스트
		else:
			self.__A = []

	# 힙 만들기
	def buildHeap(self):
		for i in range((len(self.__A) - 2) //2, -1, -1):
			self.__percolateDown(i)
    
	def findP(self, i):
		return int((i-1) / 2)
	def findC(self, i):
		return int(2*i)

	# [알고리즘 8-2] 구현: 힙에 원소 삽입하기(재귀 알고리즘 버전)
	def insert(self, x):
		A = self.__A
		A.append(x)
		self.__percolateUp(len(A) - 1)
		

  	# [알고리즘 8-2] 구현: 힙에서 원소 삭제하기
	def deleteMax(self):
		A = self.__A
		if not self.isEmpty():
			max = A[0]
			A[0] = A.pop()
			self.__percolateDown(0)
			return max
  
	# 스며오르기
	def __percolateUp(self, i:int):
		A = self.__A
		p = self.findP(i)
		if i > 0 and A[i] > A[p]:
			A[i], A[p] = A[p], A[i]
			self.__percolateUp(p)

	# 스며내리기
	def __percolateDown(self, i:int):
		A = self.__A
		cl = self.findC(i)
		cr = self.findC(i) + 1
		if cl <= (len(A)-1):
			if cr <= (len(A)-1) and A[cl] < A[cr]:
				cl = cr
			if A[i] < A[cl] :
				A[i], A[cl] = A[cl], A[i]
			self.__percolateDown(cl)

	def max(self):
		return self.__A[0]	

	# 힙이 비었는지 확인하기
	def isEmpty(self) -> bool:
		return len(self.__A) == 0

	def clear(self):
		self.__A = []

	def size(self) -> int:
		return len(self.__A)

	def heapPrint(self):
		print("Print Heap")
		if (self.isEmpty()):
			print("Heap is empty!")
		else:
			for i in range(len(self.__A)):
				print(self.__A[i], end=" ")		

# 코드 8-8