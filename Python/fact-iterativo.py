import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def facto_i(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def benchmark_iterativo(func, n, veces=1):
    """Devuelve (tiempo_promedio_en_segundos, memoria_maxima_en_MiB).
    Tiempo promedio calculado sobre 'veces' ejecuciones.
    Memoria medida con memory_usage en una sola ejecución (max_iterations=1)."""
    # medir tiempo promedio (ejecutando 'veces' veces)
    start = time.perf_counter()
    for _ in range(veces):
        resultado = func(n)
    end = time.perf_counter()
    tiempo_total = end - start
    tiempo_promedio = tiempo_total / veces

    # medir memoria (una ejecución, para obtener pico)
    mem = memory_usage((func, (n,)), max_iterations=1)
    memoria_max = max(mem) if mem else None

    return tiempo_promedio, memoria_max, resultado

if __name__ == "__main__":
    # Parámetros (ajustalos si querés)
    veces = 10000                 # cuántas repeticiones para promediar tiempo
    numeros = list(range(1, 21))  # valores de n que querés probar

    tiempos = []
    memorias = []
    resultados = []

    for n in numeros:
        tiempo_prom, mem_max, resultado = benchmark_iterativo(facto_i, n, veces=veces)
        tiempos.append(tiempo_prom)
        memorias.append(mem_max)
        resultados.append(resultado)

        print(f"n = {n}: tiempo promedio = {tiempo_prom:.10f} s, memoria pico = {mem_max} MiB, resultado (último) = {resultado}")
        print("-" * 40)

    # Gráfica tiempo
    plt.figure(figsize=(10, 5))
    plt.plot(numeros, tiempos, marker="o", label="Iterativo")
    plt.title("Tiempo promedio de ejecución (factorial iterativo)")
    plt.xlabel("n")
    plt.ylabel("Tiempo promedio (s)")
    plt.grid(True)
    plt.xticks(numeros)
    plt.legend()
    plt.savefig("tiempo_iterativo.png")
    plt.close()

    # Gráfica memoria
    plt.figure(figsize=(10, 5))
    plt.plot(numeros, memorias, marker="o", label="Memoria (pico por ejecución)")
    plt.title("Uso de memoria (factorial iterativo)")
    plt.xlabel("n")
    plt.ylabel("Memoria (MiB)")
    plt.grid(True)
    plt.xticks(numeros)
    plt.legend()
    plt.savefig("memoria_iterativo.png")
    plt.close()
