# Contador de pares
contador_pares = 0

# Entrada de datos
for i in range(5):
    numero = int(input(f"Ingresa el número {i+1}: "))
    # Condición para saber si es par
    if numero % 2 == 0:
        contador_pares += 1

# Salida
print("Cantidad de números pares:", contador_pares)