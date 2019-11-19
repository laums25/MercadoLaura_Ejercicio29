#include <iostream>
#include <cmath>

//Modificado de: https://www.dreamincode.net/forums/topic/125770-simulating-diffusion-equation/
//Guiado de: https://github.com/vostertag/solving-the-heat-equation/blob/master/computationalMethods/FTCS.cpp
//Guiado de: https://warwick.ac.uk/fac/cross_fac/complexity/study/msc_and_phd/co906/co906online/lecturenotes_2009/chap3.pdf

FILE *output;
int main (){
    int nx=100;
    int nt=100;
	double m=0.5;
    double s=0.08;
    double deltax=1.0/nx;
    double D=1.0;
    double deltat=deltax*deltax/2*D;
    double C[nx][nt];
    double x=0.0;
    int i=0;
	int j=0;
    
    output=fopen("Ejercicio29.dat", "w");

    for(i=0; i < nx; i++){                           
        x=i*deltax;
        C[i][0]=exp(-((x-m)*(x-m))/(2.0*(s*s)))/pow((2.0*M_PI*(s*s)),0.5);
    }
    C[0][0]=0.0;
    C[nx-1][0]=0.0;
                                           
    for(j = 0; j < nt - 1; j++){
        for(i=1; i<nx-1; i++){
            x=i*deltax;
            C[i][j+1] = C[i][j] + (D*deltat/(deltax*deltax))*(C[i+1][j-1] - 2*C[i][j-1] + C[i-1][j-1]);
        }                                             
        C[0][j+1]=0.0;                                      
        C[nx-1][j+1]=0.0;                          

    }

    for (i = 0; i < nx; ++i)
    {
        x = i * deltax;
        fprintf(output, "%e\t", x);
        for (j = 0; j < nt; ++j)
        {
            fprintf(output, "%e\t", C[i][j]);
            
        }
        fprintf(output, "\n");
    }                                             

    fflush(output);
    fclose(output);

    return 0;                                     
}
