# Recorremos todo el rango de números
for numero in range(1, 21):
    # El operador % devuelve el resto de la división; si es 0, es par
    if numero % 2 == 0:
        # Imprimimos solo si cumple la condición
        print(numero)