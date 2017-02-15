#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import argparse
import csv

parser = argparse.ArgumentParser()
parser.add_argument("file",help="Path to the CSV file")
parser.add_argument("num",help="Number of elements in the list")
parser.add_argument("-m","--mean", help="Print mean", action="store_true")

args = parser.parse_args()
sys.setrecursionlimit(500000)

def main(argv=None):
	if argv is None:
		argv = sys.argv
	val = 0
	cpt = 0
	with open(args.file) as csvfile:
		reader = csv.reader(csvfile, delimiter=',')
		for row in reader:
			if row[0] == args.num:
				val = val + float(row[1])
				cpt = cpt + 1

	if args.mean:
		print(val/cpt)


if __name__ == "__main__":
    main()



