#include<stdlib.h>
#include<stdio.h>

 int julia(double Zre, double Zim, double Cre, double Cim,int maxit)
 {
 	double new_Zre;
 	double new_Zim;

 	for (int i = 0; i < maxit; ++i)
 	{
 		new_Zre = Zre;
 		new_Zim = Zim;

 		Zre = new_Zre*new_Zre - new_Zim*new_Zim + Cre;
 		Zim = 2*new_Zim*new_Zre + Cim;

 		if ((Zre*Zre + Zim*Zim)>4)	
 		{
 			return i;
 		}

 	}
 	return maxit;
 }
