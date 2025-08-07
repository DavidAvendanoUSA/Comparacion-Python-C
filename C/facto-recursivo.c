#include <stdio.h>
#include <time.h>

long long facto_recursivo(int n) {  
    if (n < 0) {
        printf("Error\n");
        return -1;
    } else if (n == 0) {
        return 1;
    } else {
        return n * facto_recursivo(n - 1);
    }
}

int main() {
    int repeticiones = 10000;  
    double tiempos_promedio[20];  

    for (int n = 1; n <= 20; n++) {
        long long resultado = 0;  
        clock_t inicio = clock();

        resultado = facto_recursivo(n);
        
        for (int i = 0; i < repeticiones - 1; i++) {
            facto_recursivo(n);
        }

        clock_t fin = clock();
        
        double tiempo_total = (double)(fin - inicio) / CLOCKS_PER_SEC;
        double tiempo_promedio = tiempo_total / repeticiones;
        tiempos_promedio[n-1] = tiempo_promedio;
        
        printf("Para n = %2d:\n", n);
        printf("  Tiempo total: %.6f segundos\n", tiempo_total);
        printf("  Tiempo promedio: %.10f segundos\n", tiempo_promedio);
        printf("  Resultado: %lld\n", resultado);  
        printf("----------------------------------------\n");
    }
    return 0;
}