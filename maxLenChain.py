
class Pair(object):
	def __init__(self, a, b):
		self.a = a
		self.b = b

def maxChainLength(arr, n):
	
	max = 0

	mcl = [1 for i in range(n)]
	for i in range(1, n):
		for j in range(0, i):
			if (arr[i].a > arr[j].b and
				mcl[i] < mcl[j] + 1):
				mcl[i] = mcl[j] + 1

	for i in range(n):
		if (max < mcl[i]):
			max = mcl[i]

	return max
arr = [Pair(5, 24), Pair(15, 25),
	Pair(27, 40), Pair(50, 60)]

print('Length of maximum size chain is',
	maxChainLength(arr, len(arr)))

