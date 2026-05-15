# Primer dato como referencia
numero_menor = int(input("Ingresa el número 1: "))

# Resto de datos
for i in range(2, 11):
    numero_actual = int(input(f"Ingresa el número {i}: "))
    # Actualizamos si encontramos uno menor
    if numero_actual < numero_menor:
        numero_menor = numero_actual

print("El número menor es:", numero_menor)