#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import time
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("path",help="Path to the test files")
parser.add_argument("algo", help="Sorting algorithm [quick|quickSeuil|quickRandom|quickRandomSeuil]")
parser.add_argument("depth",type=int, help="Recursivity depth", default=1)	
parser.add_argument("-t","--time", help="Print time", action="store_true")
parser.add_argument("-p","--printn", help="Print sorted content", action="store_true")

args = parser.parse_args()
sys.setrecursionlimit(500000)

entry = []

def createEntry(t,v):
	entry.append(t)
	return entry.append(v)

def printTime(func):
	def wrapper(*args):
		# Pré-traitement
		start_time = time.clock()
		val = func(*args)
		# Post-traitement
		recordedTime = time.clock() - start_time
		createEntry(recordedTime, val)
		return entry
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
        return insertion_sort(arr)
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
	return quickSort(arr, firstElemPivot, args.depth)

def quickRandom(arr):
	return quickSort(arr, randPivot, args.depth)

def quickSeuil(arr):
	return quickSort(arr, firstElemPivot, args.depth)

def quickRandomSeuil(arr):
	return quickSort(arr, randPivot, args.depth)

def selection_sort(lst):
    for i, e in enumerate(lst):
        mn = min(range(i,len(lst)), key=lst.__getitem__)
        lst[i], lst[mn] = lst[mn], e
    return lst


def insertion_sort(k):
    for i in range(1,len(k)):    #since we want to swap an item with previous one, we start from 1
        j = i                    #bcoz reducing i directly will mess our for loop, so we reduce its copy j instead
        while j > 0 and k[j] < k[j-1]: #j>0 bcoz no point going till k[0] since there is no value to its left to be swapped
            k[j], k[j-1] = k[j-1], k[j] #syntactic sugar: swap the items, if right one is smaller.
            j=j-1 #take k[j] all the way left to the place where it has a smaller/no value to its left.
    return k

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
	F = open(args.path,"r")
	val = F.readlines()
	val = list(map(int, val))
	entry = delegator(globals()[args.algo],val)

	# if args.depth:
	# 	print('Algo',args.algo,'Seuil',args.depth)
	if args.time:
	 	print(entry[0])
 	if args.printn:
		print((str(entry[1]).replace(",","\n"))[1:-1])

if __name__ == "__main__":
    main()



