program fibonacci
implicit none
integer,parameter:: N = 100
integer :: i
double precision,dimension(N):: A

DO I=1,N
 IF (I.EQ.1) THEN
    A(I) = 0.
 ELSEIF (I.EQ.2) THEN
    A(I) = 1.
 ELSE 
    A(I) = A(I-1) + A(I-2)
 ENDIF
      ENDDO
open(7,file='fibo.dat',action='write')
write(7,*) A(:)
close(7)
end program

