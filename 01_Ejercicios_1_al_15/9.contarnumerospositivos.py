# Contador de positivos
contador_positivos = 0

# Pedimos 5 valores
for i in range(5):
    numero = int(input(f"Ingresa el número {i+1}: "))
    # Verificamos si es mayor que cero
    if numero > 0:
        contador_positivos += 1

# Resultado
print("Cantidad de números positivos:", contador_positivos)