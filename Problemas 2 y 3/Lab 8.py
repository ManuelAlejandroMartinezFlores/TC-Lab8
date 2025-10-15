import time

def function2(n):
    if n <= 0:
        return
    count = 0
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            count += 1
            break  
    return count

# Prueba de profiling
def profile_function2():
    test_values = [1, 10, 100, 1000, 10000, 100000, 1000000]
    results = []
    
    print("=== PROFILING PROBLEMA 2 ===")
    print("n\t\tTiempo (s)\tOperaciones")
    print("-" * 40)
    
    for n in test_values:
        start_time = time.time()
        operations = function2(n)
        end_time = time.time()
        execution_time = end_time - start_time
        
        results.append((n, execution_time, operations))
        print(f"{n:8d}\t{execution_time:.6f}\t{operations:8d}")
    
    return results

# Ejecutar profiling
print("----Ejercicio 2 -------")
results = profile_function2()
import matplotlib.pyplot as plt

def plot_results(results):
    n_values = [r[0] for r in results]
    times = [r[1] for r in results]
    
    plt.figure(figsize=(10, 6))
    plt.plot(n_values, times, 'bo-', linewidth=2, markersize=6)
    plt.xscale('log')
    plt.yscale('log')
    plt.xlabel('Tamaño de entrada (n) - Escala logarítmica')
    plt.ylabel('Tiempo de ejecución (segundos) - Escala logarítmica')
    plt.title('Problema 2: Complejidad O(n) - Tiempo vs Tamaño de entrada')
    plt.grid(True, alpha=0.3)
    
    # Añadir línea de referencia O(n)
    reference_n = [n_values[0], n_values[-1]]
    reference_time = [times[0], times[0] * (n_values[-1] / n_values[0])]
    plt.plot(reference_n, reference_time, 'r--', label='Referencia O(n)')
    plt.legend()
    
    plt.savefig('problema2_complejidad.png', dpi=300, bbox_inches='tight')
    plt.show()

# Generar gráfica
plot_results(results)

import time

def function3(n):
    count = 0
    for i in range(1, n//3 + 1):
        for j in range(1, n + 1, 4):
            count += 1  
    return count

def profile_function3():
    test_values = [1, 10, 100, 1000, 10000]  # Reducido por tiempo de ejecución
    results = []
    
    print("=== PROFILING PROBLEMA 3 ===")
    print("n\t\tTiempo (s)\tOperaciones")
    print("-" * 40)
    
    for n in test_values:
        start_time = time.time()
        operations = function3(n)
        end_time = time.time()
        execution_time = end_time - start_time
        
        results.append((n, execution_time, operations))
        print(f"{n:8d}\t{execution_time:.6f}\t{operations:8d}")
    
    return results

# Ejecutar profiling
results = profile_function3()

import matplotlib.pyplot as plt

def plot_results_problema3(results):
    n_values = [r[0] for r in results]
    times = [r[1] for r in results]
    operations = [r[2] for r in results]
    
    # Gráfica 1: Tiempo vs n
    plt.figure(figsize=(12, 5))
    
    plt.subplot(1, 2, 1)
    plt.plot(n_values, times, 'ro-', linewidth=2, markersize=6)
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Tiempo de ejecución (segundos)')
    plt.title('Problema 3: Tiempo vs n')
    plt.grid(True, alpha=0.3)
    
    # Gráfica 2: Operaciones vs n (escala logarítmica)
    plt.subplot(1, 2, 2)
    plt.loglog(n_values, operations, 'go-', linewidth=2, markersize=6, label='Operaciones reales')
    
    # Línea de referencia O(n²)
    reference_ops = [n**2 for n in n_values]
    plt.loglog(n_values, reference_ops, 'b--', label='Referencia O(n²)')
    
    plt.xlabel('Tamaño de entrada (n)')
    plt.ylabel('Número de operaciones')
    plt.title('Problema 3: Crecimiento O(n²)')
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('problema3_complejidad.png', dpi=300, bbox_inches='tight')
    plt.show()

# Generar gráfica
plot_results_problema3(results)