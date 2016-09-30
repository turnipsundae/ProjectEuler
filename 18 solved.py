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
# Solved: Giant for loop to generate all possible sequences
#
# Create a for loop for each layer of the data
# Each layer below can only be the same position or 1 position to the 
# right. To access the 1st number in row 3, you must pull data[2][0]
# 
########################################################################

largest = 0

for a in range(0, 1):
	for b in range(0, 2):
		for c in range(b, b + 2):
			for d in range(c, c + 2):
				for e in range(d, d + 2):
					for f in range(e, e + 2):
						for g in range(f, f + 2):
							for h in range(g, g + 2):
								for i in range(h, h + 2):
									for j in range(i, i + 2):
										for k in range(j, j + 2):
											for l in range(k, k + 2):
												for m in range(l, l + 2):
													for n in range(m, m + 2):
														for o in range(n, n + 2):
															seq = data[0][a] + data[1][b] + data[2][c] + data[3][d] + data[4][e] + data[5][f] + data[6][g] + data[7][h] + data[8][i] + data[9][j] + data[10][k] + data[11][l] + data[12][m] + data[13][n] + data[14][o]
															if seq > largest:
																largest = seq
print largest


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
# 0, 0, 0, 0
# 0, 0, 0, 1
# 0, 0, 1, 1
# 0, 0, 1, 2
# 0, 1, 1, 1
# 0, 1, 1, 2
# 0, 1, 2, 2
# 0, 1, 2, 3


def next_num(n):
	if n == 0:
		return n
	return n, n - 1

def generate_sequence_sum(a):
	# init sequence
	sequence = []
	# determine number of layers
	layers = len(a)

	# generate first sequence
	# while the length of sequence < layers
	for layer in range(0, layers):
		# determine which item to choose
		temp_sequence = []
		temp_sequence.append(layer)

		for num in range(0, l):
			temp_sequence.append(num)
		sequence.append(temp_sequence)

	# for layer2 in range(3, 0, -1):
	# 	temp_sequence = []
	# 	for layer1 in range(layer2 - 1, 0, -1):
	# 		temp_sequence.append(layer1)
	# 	temp_sequence.append(layer2)
	# 	sequence.append(temp_sequence)




	return sequence
	# return sequence