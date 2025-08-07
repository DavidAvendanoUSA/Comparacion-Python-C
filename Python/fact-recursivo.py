import time
import matplotlib.pyplot as plt
from memory_profiler import memory_usage

def factorial_recursivo(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)

veces = 10000
tiempos = []
memoria_promedio = []
memoria_pico = []

numeros = list(range(1, 21))

print("🔍 Iniciando análisis de tiempo y memoria...")
print("=" * 60)

for numero in numeros:

    inicio = time.time()

    mem_usage = memory_usage((lambda: [factorial_recursivo(numero) for _ in range(veces)]),
                              max_usage=True, retval=True)

    fin = time.time()

    total_tiempo = fin - inicio
    promedio_tiempo = total_tiempo / veces

    resultado = factorial_recursivo(numero)

    max_mem = mem_usage[0]
    avg_mem = max_mem / veces

    tiempos.append(promedio_tiempo)
    memoria_promedio.append(avg_mem)
    memoria_pico.append(max_mem)

    print(f"Para n = {numero}:")
    print(f"Tiempo total: {total_tiempo:.6f} segundos")
    print(f"Tiempo promedio: {promedio_tiempo:.10f} segundos")
    print(f"Memoria promedio por llamada: {avg_mem:.6f} MB")
    print(f"Pico máximo de memoria: {max_mem:.6f} MB")
    print(f"Resultado: {resultado}")
    print("-" * 60)

print("\nGenerando gráficos de análisis...")


plt.style.use('ggplot')
fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15))

ax1.plot(numeros, tiempos, 'o-', color='#1f77b4', linewidth=2, markersize=8)
ax1.set_title('Tiempo Promedio por Ejecución', fontsize=16, pad=20)
ax1.set_xlabel('Valor de n', fontsize=12)
ax1.set_ylabel('Segundos', fontsize=12)
ax1.grid(True, linestyle='--', alpha=0.7)
ax1.set_xticks(numeros)
ax1.set_yscale('log')


ax2.plot(numeros, memoria_promedio, 's-', color='#2ca02c', linewidth=2, markersize=8)
ax2.set_title('Memoria Promedio por Llamada', fontsize=16, pad=20)
ax2.set_xlabel('Valor de n', fontsize=12)
ax2.set_ylabel('Megabytes (MB)', fontsize=12)
ax2.grid(True, linestyle='--', alpha=0.7)
ax2.set_xticks(numeros)


ax3.bar(numeros, memoria_pico, color='#d62728', alpha=0.7)
ax3.set_title('Pico Máximo de Memoria por Conjunto de Ejecuciones', fontsize=16, pad=20)
ax3.set_xlabel('Valor de n', fontsize=12)
ax3.set_ylabel('Megabytes (MB)', fontsize=12)
ax3.grid(True, linestyle='--', alpha=0.7)
ax3.set_xticks(numeros)

plt.tight_layout(pad=3.0)
plt.savefig("analisis_factorial_recursivo.png", dpi=150)
plt.show()
