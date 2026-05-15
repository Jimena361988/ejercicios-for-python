# Acumulador
suma = 0
# Cantidad fija de números
cantidad = 5

# Entrada de datos
for i in range(cantidad):
    numero = int(input(f"Ingresa el número {i+1}: "))
    suma += numero

# Cálculo del promedio
promedio = suma / cantidad
# Imprimir resultado
print("El promedio es:", promedio)