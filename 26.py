import re

def primes_up_to(n):
	# list of primes
	primes = [2]
	for i in range(3,n):
		for prime in primes:
			if i % prime == 0:
				break
		else:
			primes.append(i)
	return primes


# 1 / d for primes up to 1000
D = [1.0/prime for prime in primes_up_to(1000)]
# print (D)

def recurring_digits(digits):
	digits = str(digits)
	RE = re.compile(r'.[0]+')
	digits = RE.split(digits, 2)[-1]
	# print digits
	# given '1234512345'
	# look at digit #1, compare to #2
	# if not the same, (1 != 2) extend base to first 2 digits '12'
	# continue to compare and extend
	# once you match where length of base ends at the starting position of the next, you're good
	recurring = digits[0]
	for i in range(1,len(digits)):
		if recurring == digits[i:i+len(recurring)] and len(digits.split(recurring)[-1]) == 0:
			break
		else:
			recurring = digits[:i+1]
	return recurring

# print (recurring_digits('0.0010559662090813093'))

l = 0
for p in primes_up_to(1000):
	print (p, 1.0/p, recurring_digits(1.0/p))