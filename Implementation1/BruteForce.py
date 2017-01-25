import math
'''
	CS 325 - Implementation 1
		Brute Force

	Kyle Prouty
	Winter 2017
'''
inputfile = "points.input"

def readFile():
	lst =[]
	with open(inputfile) as file:
		lst = [tuple(map(int, l.split(' '))) for l in file]
	return lst


def distance(tupA, tupB):
	return math.sqrt((tupB[0]-tupA[0])**2 + (tupB[1]-tupA[1])**2)


def bruteForce(lst):
	min = float("inf")
	for tupA in lst:
		for tupB in lst:
			d = distance(tupA, tupB)
			if (d != 0) and (d <= min): 
				min = d
	return min
	

def printMinDistance(lst):
	min = bruteForce(lst)
	print min
	
	'''
	lst.sort(key=lambda x: x[1])
	lst.sort(key=lambda x: x[0])
	for a in lst:
		for b in lst:
			if distance(a,b) == min:
				tmp = [a,b]
				if tmp[0][1] > tmp[1][1]:
					print b, a
	'''

printMinDistance( readFile() )