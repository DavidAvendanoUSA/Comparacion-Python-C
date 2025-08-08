# Comparación de eficiencia: Factorial Iterativo vs Recursivo

## Descripción
En esta práctica comparamos dos enfoques para calcular el factorial de un número entero (*n!*):  
- **Iterativo**  
- **Recursivo**

Se implementaron ambos enfoques en **Python** y en **C**, y para cada implementación se midió:  
- **Tiempo promedio de ejecución**  
- **Uso máximo de memoria**

El objetivo es analizar y comparar la eficiencia (tiempo y memoria) entre ambos enfoques en los dos lenguajes.

---

## Índice
- [Introducción](#descripción)  
- [Resultados y análisis](#resultados-y-análisis)  
  - [Python](#python)  
  - [C](#c)  
- [Conclusión](#conclusión)  
- [Figuras](#figuras)

---

## Resultados y análisis

### Python
- **Memoria**: Tanto el método iterativo como el recursivo mantuvieron un uso de memoria estable sin variaciones significativas al aumentar *n* (**Figura 1** y **Figura 2**).  

- **Tiempo**: El método **iterativo** mostró tiempos promedio menores que el recursivo para la mayoría de valores de *n*; ambos métodos crecen ligeramente conforme aumenta *n* (**Figura 3** y **Figura 4**).

---

### C
- **Memoria**: Ambos métodos presentaron un consumo muy bajo y estable; se observó un pico inicial en *n = 1* por la inicialización del programa (**Figura 5** y **Figura 6**).  

- **Tiempo**: De nuevo, el método **iterativo** fue ligeramente más rápido que el recursivo; las diferencias son pequeñas (orden de nanosegundos) pero consistentes (**Figura 7** y **Figura 8**).

---

## Conclusión
- **Iterativo**: Más eficiente en tiempo tanto en Python como en C.  
- **Recursivo**: Código más claro y directo, pero con un ligero sobrecoste en tiempo por las llamadas recursivas.  
- **Memoria**: No se observaron diferencias relevantes en el rango de *n* analizado (1–20).  
- **Recomendación**: Para rendimiento y escalabilidad usar iterativo; para claridad o enseñanza, la recursividad es adecuada.

---

## Figuras

### Python — Memoria

**Figura 1:** Memoria (iterativo en Python)  
<img width="1000" height="500" alt="memoria_iterativo" src="https://github.com/user-attachments/assets/314f08d7-c743-4855-9b03-c86b79035177" />

**Figura 2:** Memoria (recursivo en Python)  
<img width="1000" height="500" alt="memoria_recursivo" src="https://github.com/user-attachments/assets/a05311a6-0a99-47ec-9ca3-f2ca02670f21" />

---

### Python — Tiempo

**Figura 3:** Tiempo (iterativo en Python)  
<img width="1000" height="500" alt="tiempo_iterativo" src="https://github.com/user-attachments/assets/6719e0c9-f223-44e0-8f98-c7f2fa79ab5c" />

**Figura 4:** Tiempo (recursivo en Python)  
<img width="1000" height="500" alt="tiempo_recursivo" src="https://github.com/user-attachments/assets/ed35b97f-6606-4bab-8754-c1e652343c95" />

---

### C — Memoria

**Figura 5:** Memoria (iterativo en C)  
<img width="480" height="282" alt="memoria_iterativo_c" src="https://github.com/user-attachments/assets/e07d6a10-1d71-4ed7-af54-34aee0a633c6" />

**Figura 6:** Memoria (recursivo en C)  
<img width="482" height="284" alt="memoria_recursivo_c" src="https://github.com/user-attachments/assets/724f6081-bbc9-4e99-b38f-240fdfe76bba" />

---

### C — Tiempo

**Figura 7:** Tiempo (iterativo en C)  
<img width="481" height="290" alt="Tiempo_iterativo_c" src="https://github.com/user-attachments/assets/4da657d2-8c88-4ba7-9648-c9238ac3cc3e" />

**Figura 8:** Tiempo (recursivo en C)  
<img width="478" height="286" alt="tiempo_recursivo_c" src="https://github.com/user-attachments/assets/df840a16-bee4-442e-969e-e62ec76f6a19" />
