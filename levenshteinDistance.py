import math 

SENTINEL      = -1
DELETE_COST   = 1
INSERT_COST   = 1
SUBSTITUTION_COST = 1

def min(a,b,c):
	min = a
	if min > b:
		min = b
	if min > c:
		min = c
	return min

def pintMatrix(matrix):
	for row in matrix:
		print(row)

def levenshteinDistance(a,b):
	cost = 0
	rowsLen = len(a) + 1
	colsLen = len(b) + 1

	matrix = [[SENTINEL for col in range(colsLen)] for row in range(rowsLen)]

	for i in range(rowsLen):
		matrix[i][0] = i
	for j in range(colsLen):
		matrix[0][j] = j	

	for i in range(1,rowsLen):
		for j in range(1,colsLen):
			deleteCost = matrix[i - 1][j] + DELETE_COST
			insertCost = matrix[i][j - 1] + INSERT_COST

			subStitutionCost = matrix[i - 1][j - 1] + (a[i-1] != b[j-1] and 1 or 0) 

			matrix[i][j] = min(deleteCost,insertCost,subStitutionCost)

	cost = matrix[rowsLen - 1][colsLen - 1]
	return cost
print(levenshteinDistance("kitten","sitting"))