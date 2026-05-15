# Inicializamos con el primer valor ingresado
numero_mayor = int(input("Ingresa el número 1: "))

# Ingresamos los 9 números restantes
for i in range(2, 11):
    numero_actual = int(input(f"Ingresa el número {i}: "))
    # Comparamos y actualizamos si es mayor
    if numero_actual > numero_mayor:
        numero_mayor = numero_actual

print("El número mayor es:", numero_mayor)