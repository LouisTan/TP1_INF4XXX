from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import sys

def drawGraph(file1,file2,file3):

	x,y = np.loadtxt(str(file1)+".csv", 
					 delimiter = ',',
				   	 unpack = True)

	x1,y1 = np.loadtxt(str(file2)+".csv", 
					 delimiter = ',',
				   	 unpack = True)

	x2,y2 = np.loadtxt(str(file3)+".csv", 
					 delimiter = ',',
				   	 unpack = True)

	plt.plot(x,y,'go',label=file1)
	plt.plot(x1,y1,'ro',label=file2)
	plt.plot(x2,y2,'ko',label=file3)

	plt.title(str(file1)+" vs "+str(file2)+" vs "+str(file3))
	plt.ylabel('Temps execution (s)')
	plt.xlabel('Nombre operations')
	plt.legend(loc='best')
	
 	plt.show()

def main(argv=None):
	if argv is None:
		argv = sys.argv

	drawGraph(sys.argv[1], sys.argv[2], sys.argv[3])
if __name__ == "__main__":
    main()




