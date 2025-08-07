import time

def factorial_recursivo(n):
    if n < 0:
        return "error"
    elif n == 0:
        return 1
    else:
        return n * factorial_recursivo(n - 1)


veces = 10000  
tiempos = []

for numero in range(1, 21):

    inicio = time.time()
    
    for i in range(veces):
        resultado = factorial_recursivo(numero)
    
    fin = time.time()
    
    total_tiempo = fin - inicio
    promedio_tiempo = total_tiempo / veces
    
    
    tiempos.append(promedio_tiempo)
    
    print(f"Para n = {numero}:")
    print(f"  Tiempo total: {total_tiempo:.4f} segundos")
    print(f"  Tiempo promedio: {promedio_tiempo:.8f} segundos")
    print(f"  Resultado: {resultado}")  
    print("-" * 30)

