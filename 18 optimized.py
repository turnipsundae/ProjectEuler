########################################################################
# reformat raw data into array
########################################################################
triangle = """75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23"""
data = []
for row in triangle.split("\n"):
	temp = row.split(" ")
	i = 0
	while i < len(temp):
		temp[i] = int(temp[i])
		i += 1
	data.append(temp)


########################################################################
# examples of different sequences
########################################################################
#  3
# 7 4
#
# 0, 0
# 0, 1
########################################################################
#   3
#  7 4
# 2 4 6
#
# 0, 0, 0
# 0, 0, 1
# 0, 1, 1
# 0, 1, 2
########################################################################
#    3
#   7 4
#  2 4 6
# 8 5 9 3
#
# 0, 0, 0, 0 (0,0; 1,0; 2,0; 3,0)
# 0, 0, 0, 1
# 0, 0, 1, 1
# 0, 0, 1, 2
# 0, 1, 1, 1
# 0, 1, 1, 2
# 0, 1, 2, 2
# 0, 1, 2, 3

def reverse_list(lst):
	for i in range(0, len(lst)/2):
		lst[i] , lst[len(lst) - 1 - i] = lst[len(lst) - 1 - i], lst[i]	

def generate_sequence_sum(a):
	"""
	Takes a triangle list in reverse and returns the largest sum
	of possible paths.
	"""
	# determine number of layers
	layers = len(a)
	# init vars
	r, c = 0, 0
	# Starting from the bottom row, compare the first two elements to
	# find which is larger. Add the larger one to the parent element.
	# March through each pair of elements until the row is finished,
	# then traverse up the rows. The largest sum is the end element.
	while r < layers - 1:
		while c < len(data[r + 1]):
			x = data[r + 1][c]
			data[r + 1][c] = max(data[r][c] + x, data[r][c + 1] + x)
			c += 1
		c = 0
		r += 1
	return data[layers - 1][0]

reverse_list(data)
print generate_sequence_sum(data)