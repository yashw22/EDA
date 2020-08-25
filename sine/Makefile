findsine: findsine.o
	gfortran -o findsine findsine.o
findsine.o: findsine.f90
	gfortran -c -g -ffree-line-length-none findsine.f90
clean:
	rm -f findsine.o findsine.exe
