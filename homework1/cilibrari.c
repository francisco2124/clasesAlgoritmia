/*#include <stdio.h>

void display(char* name, int age){
    printf("Hello world :D my name is %s and my age is %s", name, age);
}

*/

#include <stdio.h>
#include <stdlib.h>

void cprint_array(int a[], int m){
    int i;
    for(i=0; i < m; i++){
        //arr[i] = 2*arr[i];
        printf("%i ", a[i]);
    }
    printf("\n");
    
}