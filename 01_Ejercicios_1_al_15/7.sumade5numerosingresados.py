# Variable para ir guardando la suma
suma_total = 0

# Repetimos 5 veces el proceso
for i in range(5):
    # Pedimos dato al usuario
    numero = int(input(f"Ingresa el número {i+1}: "))
    # Agregamos el valor a la suma
    suma_total += numero

# Resultado final
print("Suma total:", suma_total)