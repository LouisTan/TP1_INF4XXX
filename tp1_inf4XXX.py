#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Les fonctions de tri proviennent de :
# http://rosettacode.org/wiki/Sorting_algorithms

import sys
import time
import random
import re

sys.setrecursionlimit(500000)

def printTime(func):
	def wrapper(*args):
		# Pré-traitement
		start_time = time.clock()
		val = func(*args)
		for x in range(1,len(sys.argv)):
			if sys.argv[x] == "-t":
				print (time.clock() - start_time)
		return val
	return wrapper
	
@printTime
def delegator(func, val):
	return func(val)

def randPivot(arr):
	return random.choice(arr)

def firstElemPivot(arr):
	return arr[0]

def quickSort(arr, funcPivot, limit):
    less = []
    pivotList = []
    more = []
    if len(arr) <= limit:
        return selection_sort(arr)
    else:
        pivot = funcPivot(arr)
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
               pivotList.append(i)
        less = quickSort(less, funcPivot, limit)
        more = quickSort(more, funcPivot, limit)
        return less + pivotList + more

def quick(arr):
	return quickSort(arr, firstElemPivot, 1)

def quickRandom(arr):
	return quickSort(arr, randPivot, 1)

def quickSeuil(arr):
	return quickSort(arr, firstElemPivot, 20)

def quickRandomSeuil(arr):
	return quickSort(arr, randPivot, 20)

def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst

def counting(array):
	from collections import defaultdict
	count = defaultdict(int)
	for i in array:
		count[i] += 1
	result = []
	for j in array:
		result += [j]* count[j]
	return result
 
def main(argv=None):
	if argv is None:
		argv = sys.argv
	F = open(argv[1],"r")
	val = F.readlines()
	val = list(map(int, val))
	val = delegator(globals()[argv[2]], val)

	for x in range(1,len(sys.argv)):
		if sys.argv[x] == "-p":
			val = str(val)
			val = val.replace(",","\n")
			print((val)[1:-1])

if __name__ == "__main__":
    main()


