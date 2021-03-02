#include <omp.h>
#include <stdio.h>

int main (int argc, char *argv[])
{
  #pragma omp parallel 
  {
    int var = 10;
    var = var + omp_get_thread_num();
    printf("Hello World from thread: %d, var is %d\n", omp_get_thread_num(), var);
  }
}
