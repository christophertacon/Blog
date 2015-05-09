SUBROUTINE FIB(A,N)
INTEGER,intent(in):: N
Double precision,dimension(N),intent(inout) :: A
DO I=1,N
 IF (I.EQ.1) THEN
    A(I) = 0.
 ELSEIF (I.EQ.2) THEN
    A(I) = 1.
 ELSE 
    A(I) = A(I-1) + A(I-2)
 ENDIF
      ENDDO
END
