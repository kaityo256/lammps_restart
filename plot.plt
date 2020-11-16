set term png
set out "plot.png"
set style data linespoints
set xlabel "Steps"
set ylabel "Temperature"
p "runall.dat" pt 6 t "Run All", "restart.dat" pt 4 t "Restart"
