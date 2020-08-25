program sine
  implicit none
  real :: rad
  real :: deg
  deg = 60
  rad = deg*11/630
  write(*,*) "Sine of 60 degrees is:", SIN(rad)
  
end program sine
