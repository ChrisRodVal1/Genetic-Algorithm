import numpy as np

# Definir la función objetivo
def f(x):
    return (x - 3) ** 2 + 4  # Función a minimizar

# Obtener parámetros del usuario
GENERATIONS = int(input("Ingrese el número de interaciones: "))  # Número de interaciones
x_range_input = input("Ingrese el rango de valores de x (Ejemplo: 0,2): ")  # Rango de valores de x
X_RANGE = tuple(map(int, x_range_input.split(',')))  # Convertir el rango en una tupla de enteros

# Parámetros del algoritmo genético
POP_SIZE = 20  # Tamaño de la población
MUTATION_RATE = 0.1  # Probabilidad de mutación

# Inicializar población aleatoria
population = np.random.uniform(X_RANGE[0], X_RANGE[1], POP_SIZE)

# Función de selección (elige los mejores individuos)
def select(pop):
    scores = np.array([f(x) for x in pop])  # Evaluar población
    idx = np.argsort(scores)  # Ordenar por menor valor de f(x)
    return pop[idx[:POP_SIZE // 2]]  # Retorna la mitad mejor

# Función de cruce (crossover)
def crossover(parents):
    children = []
    for _ in range(len(parents) // 2):
        p1, p2 = np.random.choice(parents, 2, replace=False)
        child = (p1 + p2) / 2  # Promedio de los padres
        children.append(child)
    return np.array(children)

# Función de mutación
def mutate(pop):
    for i in range(len(pop)):
        if np.random.rand() < MUTATION_RATE:
            pop[i] += np.random.uniform(-1, 1)  # Pequeño cambio aleatorio
    return np.clip(pop, X_RANGE[0], X_RANGE[1])  # Asegurar que esté en rango

# Algoritmo Genético Principal
for gen in range(GENERATIONS):
    selected = select(population)  # Selección de los mejores
    children = crossover(selected)  # Cruzamiento
    mutated = mutate(children)  # Mutación
    population = np.concatenate((selected, mutated))  # Nueva población

# Encontrar la mejor solución final
best_x = population[np.argmin([f(x) for x in population])]
best_f = f(best_x)

print(f"Valor óptimo de x: {best_x}")
print(f"Valor mínimo de f(x): {best_f}")
