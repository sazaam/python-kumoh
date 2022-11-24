from ast import Pass


def heapSort(A):
	buildHeap(A)
	for last in range(len(A)-1, 0, -1) :
		A[last], A[0] = A[0], A[last]
		percolateDown(A, 0, last - 1)
	

def buildHeap(A):
	for i in range((len(A)-2) // 2, -1, -1) :
		percolateDown(A, i, len(A)-1)

def percolateDown(A, k:int, end:int):
	child = 2*k+1	 # 왼자식
	right = 2*k+2	 # 오른자식
	if child <= end:
			if right <= end and A[child] < A[right]:
				child = right
			if A[k] < A[child]:
				A[k], A[child] = A[child], A[k]
				percolateDown(A, child, end)

# 코드 9-7