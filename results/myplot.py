from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np
import sys

def drawGraph(file1,file2):
	x,y = np.loadtxt(str(file1)+".csv", 
					 delimiter = ',',
				   	 unpack = True)

	x1,y1 = np.loadtxt(str(file2)+".csv", 
					 delimiter = ',',
				   	 unpack = True)

	plt.plot(x,y,'r--',label=file1)
	plt.plot(x1,y1,'b-',label=file2)

	plt.title(str(file1)+" vs "+str(file2))
	plt.ylabel('Vitesse dexecution (s)')
	plt.xlabel('Nombre doperations')
	plt.legend(loc='best')
	
 	plt.show()

def main(argv=None):
	if argv is None:
		argv = sys.argv

	drawGraph(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()



