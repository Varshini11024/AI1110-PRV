
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include "coeffs.h"
#define N 1000000

int  main()
{

    //Mean of uniform 
    printf("Mean of U is %lf\n",mean("gau.dat"));
    double Mean = mean("gau.dat");

    FILE *file; double samples[N];
    file = fopen("gau.dat","r");
    if(!file)
    {
        printf("Error opening file");
        return -1;
    }

    int i=0;
    memset(samples, 0, sizeof(samples));
    while (!feof(file) )     
    {
        fscanf(file, "%lf", &(samples[i++]));
    }
    fclose(file);

    double sum=0;
    for (int i = 0; i < N; i++){
    sum+= (samples[i] - Mean)*(samples[i]-Mean);
    }

    printf("Variance of U is %lf\n", sum/N);
    return 0;
}
