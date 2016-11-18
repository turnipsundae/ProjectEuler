# print the first fib number that has 1000 digits

t = int('1' + '0' * 999)

a, b = 0, 1
c = 1
while b < t:
    a, b = b, a + b
    c += 1

print c
