# Pedimos un valor al usuario y lo convertimos a entero
numero = int(input("Ingresa un número para ver su tabla: "))

# Ciclo del 1 al 10 para multiplicar
for i in range(1, 11):
    # Calculamos el resultado
    resultado = numero * i
    # Mostramos la operación formateada
    print(f"{numero} x {i} = {resultado}")