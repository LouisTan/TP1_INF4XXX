set datafile separator “\n”
set autoscale fix
set key outside right center

set title “Graph 1”
plot ‘quick_serie1.csv’ using 4 title “Quick Serie” with lines

pause -1