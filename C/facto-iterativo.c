#include <stdio.h>
#include <time.h>

long long int facto_iterativo(int n) {
    if (n < 0) {
        printf("error\n");
        return -1;
    } else if (n == 0) {
        return 1;
    } else {
        long long int resultado = 1;
        for (int i = 1; i <= n; i++) {
            resultado *= i;
        }
        return resultado;
    }
}

int main() {
    int repeticiones = 10000;  
    double tiempos[20];  
    
    for (int n = 1; n <= 20; n++) {
        long long int resultado = 0;
        clock_t inicio = clock();
        for (int i = 0; i < repeticiones; i++) {
            volatile long long int temp = facto_iterativo(n);
            if (i == repeticiones - 1) resultado = temp;
        }

        clock_t fin = clock();
        double tiempo_total = (double)(fin - inicio) / CLOCKS_PER_SEC;
        tiempos[n-1] = tiempo_total;  
        printf("Para n = %2d:\n", n);
        printf("  Tiempo total: %.6f segundos\n", tiempo_total);
        printf("  Tiempo promedio: %.10f segundos\n", tiempo_total / repeticiones);
        printf("  Resultado: %lld\n", resultado);
        printf("----------------------------------------\n");
    }
    return 0;
}