import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def factorial_recursivo(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

def benchmark_recursivo(func, n, veces=1):
    # Medir tiempo promedio (ejecutando 'veces' veces)
    start = time.perf_counter()
    for _ in range(veces):
        resultado = func(n)
    end = time.perf_counter()
    tiempo_total = end - start
    tiempo_promedio = tiempo_total / veces

    # Medir memoria (una ejecución, para pico)
    mem = memory_usage((func, (n,)), max_iterations=1)
    memoria_max = max(mem) if mem else None

    return tiempo_promedio, memoria_max, resultado

if __name__ == "__main__":
    veces = 10000
    numeros = list(range(1, 21))

    tiempos = []
    memorias = []
    resultados = []

    for n in numeros:
        tiempo_prom, mem_max, resultado = benchmark_recursivo(factorial_recursivo, n, veces)
        tiempos.append(tiempo_prom)
        memorias.append(mem_max)
        resultados.append(resultado)

        print(f"n = {n}: tiempo promedio = {tiempo_prom:.10f} s, memoria pico = {mem_max} MiB, resultado = {resultado}")
        print("-" * 40)

    # Gráfica tiempo
    plt.figure(figsize=(10, 5))
    plt.plot(numeros, tiempos, marker="o", label="Recursivo")
    plt.title("Tiempo promedio de ejecución (factorial recursivo)")
    plt.xlabel("n")
    plt.ylabel("Tiempo promedio (s)")
    plt.grid(True)
    plt.xticks(numeros)
    plt.legend()
    plt.savefig("tiempo_recursivo.png")
    plt.close()

    # Gráfica memoria
    plt.figure(figsize=(10, 5))
    plt.plot(numeros, memorias, marker="o", label="Memoria (pico por ejecución)")
    plt.title("Uso de memoria (factorial recursivo)")
    plt.xlabel("n")
    plt.ylabel("Memoria (MiB)")
    plt.grid(True)
    plt.xticks(numeros)
    plt.legend()
    plt.savefig("memoria_recursivo.png")
    plt.close()
