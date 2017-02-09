from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import sys

def drawGraph(filename):
	x,y = np.loadtxt(filename, 
				   delimiter = ',',
				   unpack = True)
	plt.plot(x,y)

	plt.title('Epic Chart')
	plt.ylabel('Y axis')
	plt.xlabel('X axis')

 	plt.show()

def main(argv=None):
	if argv is None:
		argv = sys.argv

	drawGraph(sys.argv[1])

if __name__ == "__main__":
    main()



