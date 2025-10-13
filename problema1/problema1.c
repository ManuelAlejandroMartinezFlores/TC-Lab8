#include <stdio.h>
#include <time.h>

unsigned long long function(int n) {
    long long i, j, k;
    unsigned long long counter = 0;
    for (i = n/2; i <= n; i++) {
        for (j = 1; j+n/2 <= n; j++) {
            for (k = 1; k <= n; k = k*2) {
                counter++;
            }
        }
    }
    return counter;
}

int main() {
    int k = 1;
    printf("CPU Time:\n");
    for (k = 1; k <= 1e5; k = k*10) {
        clock_t start = clock();
        unsigned long long ops = function(k);
        clock_t end = clock();
        double cpu_time_used = ((double) (end - start)) / CLOCKS_PER_SEC;
        printf("%d\t%llu\t%f\n", k, ops, cpu_time_used);
    }
    return 0;
}