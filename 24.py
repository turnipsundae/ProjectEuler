import math

def merge2(a, b):
	return [b[:x] + a + b[x:] for x in range(0, len(b)+1)]

def merge2(a, B):
	r = []
	for b in B:
		r.extend([b[:x] + a + b[x:] for x in range(0, len(b)+1)])
	return r

def merge(a, B):
	return [[b[:x] + a + b[x:] for x in range(0, len(b)+1)] for b in B]

def permutations(num):
	num = str(num)
	if len(num) == 1:
		return num
	else:
		d, num = num[0], num[1:]
		return merge2(d, permutations(num))

n = '0123456789'
P = permutations(n)
P.sort()
print (P[999999], P[1000000])
print (len(set(P)) - math.factorial(len(n)))