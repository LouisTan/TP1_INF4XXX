from matplotlib import pyplot as plt
from textwrap import wrap
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("files",help="file1.csv file2.csv ...", nargs='+')
args = parser.parse_args()

def drawGraph():
	for ind in range(len(args.files)):
		x,y = np.loadtxt(str(args.files[ind]),delimiter = ',', unpack = True)
		plt.plot(x,y,label=args.files[ind],log=True)

# 	maxY = 0.0
# 	for ind in range(len(args.files)):
# 		x,y = np.loadtxt(str(args.files[ind]),delimiter = ',', unpack = True)
# 		plt.loglog(x,y,label=args.files[ind],marker="o",basex=2, basey=2)
# 		if y[ind] > maxY:
# 			maxY = y[ind]

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
