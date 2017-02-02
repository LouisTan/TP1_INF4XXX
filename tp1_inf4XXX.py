#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Les fonctions de tri proviennent de :
# http://rosettacode.org/wiki/Sorting_algorithms

import sys
import time
import random
import getopt

def printTime(func):
	def wrapper(*args):
		# Pré-traitement
		start_time = time.clock()
		val = func(*args)
		# Post-traitement
		return time.clock() - start_time
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
        return sorted(arr)
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
	return quickSort(arr, firstElemPivot, 500)

def quickRandomSeuil(arr):
	return quickSort(arr, randPivot, 2)

def insertion_sort(l):
    for i in xrange(1, len(l)):
        j = i-1 
        key = l[i]
        while (l[j] > key) and (j >= 0):
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key

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
	print(val)


		
if __name__ == "__main__":
    main()


