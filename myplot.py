from matplotlib import pyplot as plt
from textwrap import wrap
import numpy as np
import argparse
import sys
import math

parser = argparse.ArgumentParser()
parser.add_argument("files",help="file1.csv file2.csv ...", nargs='+')

args = parser.parse_args()

def func(n):
	return n*math.log(n, 2)

def drawGraph():
	for ind in range(len(args.files)):
		f = []
		
		x,y = np.loadtxt(str(args.files[ind]),delimiter = ',', unpack = True)	
		
		for n in range(1,len(y)+1):
			f.append(func(n))
			print("y",y[n-1])
			print("f",f[n-1])
			
		
		plt.plot(y,y/f,label=args.files[ind])
	
	plt.title("\n".join(wrap(str(args.files)[1:-1], 60)))	
	plt.ylabel('Temps d\'execution (s)')
	plt.xlabel('Nombre d\'operations')
	plt.legend(loc='best')
	
 	plt.show()

def main(argv=None):
	if argv is None:
		argv = sys.argv

	drawGraph()

if __name__ == "__main__":
    main()
