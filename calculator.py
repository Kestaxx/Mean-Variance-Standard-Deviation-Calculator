import numpy as np

lista = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

def calculado(lista):
    
    ls = np.array(lista)
    
    # Reshape la matriz para que tenga 3 filas y 3 columnas
    ls = ls.reshape(3, 3)

    # Calcula el promedio de cada fila y columna
    mean_rows = np.mean(ls, axis=1)
    mean_columns = np.mean(ls, axis=0)
    
    # Calcula el promedio de toda la matriz
    mean_all = np.mean(ls)

    # Calcula la varianza de cada fila y columna
    var_rows = np.var(ls, axis=1)
    var_columns = np.var(ls, axis=0)

    # Calcula la varianza de toda la matriz
    var_all = np.var(ls)

    # Calcula la desviacion estandar de cada fila y columna
    std_rows = np.std(ls, axis=0)
    std_columns = np.std(ls, axis=1)

    # Calcula la desviacion estandar de toda la matriz
    std_all = np.std(ls)

    # Calcula el valor maximo da cada fila y columna
    max_rows = np.max(ls, axis=0)
    max_columns = np.max(ls, axis=1)

    # Calcula el valor minimo de toda la matriz
    max_all = np.max(ls)

     # Calcula el valor minimo da cada fila y columna
    min_rows = np.min(ls, axis=0)
    min_columns = np.min(ls, axis=1)

    # Calcula el valor minimo de toda la matriz
    min_all = np.min(ls)

    # Calcula la suma de cada fila y columna
    sum_rows = np.sum(ls, axis=0)
    sum_columns = np.sum(ls, axis=1)

    # Calcula la suma de toda la matriz
    sum_all = np.sum(ls)

    # Construye los diccionarios separados para promedios, varianzas, desviacion estandar, maximos, minimos, sumas
    promedios = {
        "mean_rows": mean_rows.tolist(),
        "mean_columns": mean_columns.tolist(),
        "mean_all": mean_all,
    }

    varianzas = {
        "var_rows": var_rows.tolist(),
        "var_columns": var_columns.tolist(),
        "var_all": var_all.tolist()
    }

    std = {
        "std_rows": std_rows.tolist(),
        "std_columns": std_columns.tolist(),
        "std_all": std_all.tolist()
    }

    maximo = {
        "max_rows": max_rows.tolist(),
        "max_columns": max_columns.tolist(),
        "max_all": max_all.tolist()
    }

    minimo = {
        "min_rows": min_rows.tolist(),
        "min_columns": min_columns.tolist(),
        "min_all": min_all.tolist()
    }

    suma = {
        "sum_rows": sum_rows.tolist(),
        "sum_columns": sum_columns.tolist(),
        "sum_all": sum_all.tolist()
    }

    return promedios, varianzas, std, maximo, minimo, suma

# Llama a la función y muestra el resultado
promedios, varianzas, std, maximo, minimo, suma = calculado(lista)

# Imprime los promedios
print("Promedios:")
for key, value in promedios.items():
    print(f"{key}: {value}")

# Imprime las varianzas
print("\nVarianzas:")
for key, value in varianzas.items():
    print(f"{key}: {value}")

# Imprime las desviaciones estandar
print("\nStd:")
for key, value in std.items():
    print(f"{key}: {value}")    

# Imprime los maximos
print("\nMaximo:")
for key, value in maximo.items():
    print(f"{key}: {value}")

# Imprime los minimos
print("n\minimo:")
for key, value in minimo.items():
    print(f"{key}: {value}")    

# Imprime las sumas
print("\nSuma:")
for key, value in suma.items():
    print(f"{key}: {value}")
