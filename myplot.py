from matplotlib import pyplot as plt
from textwrap import wrap
import numpy as np
import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("files",help="Number of curves of display (MAX: 6)", nargs='+')
args = parser.parse_args()

def drawGraph():
	for ind in range(len(args.files)):
		x = "x"+str(ind)
		y = "y"+str(ind)
		x,y = np.loadtxt(str(args.files[ind]),delimiter = ',', unpack = True)
		plt.plot(x,y,label=args.files[ind])


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
