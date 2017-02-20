#!/usr/bin/env python
# -*- coding: utf-8 -*-	
import sys
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file",help="Path to the CSV file")

args = parser.parse_args()
sys.setrecursionlimit(500000)

meanList = []

def average():
	num = [1000,5000,10000,50000,100000,500000]
	
	with open(args.file) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for n in num:
			val = 0
			cpt = 0
			for row in reader:
				if str(n) == row[0]:
					val = val + float(row[1])
					cpt = cpt + 1
			entry = (n,val/cpt)
			meanList.append(entry)
			print(cpt)

			csvfile.seek(0)
	return meanList


def main(argv=None):
	if argv is None:
		argv = sys.argv


	print(average())

	

	
		
if __name__ == "__main__":
    main()



