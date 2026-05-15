# Acumulador
suma_notas = 0
cantidad_notas = 5

# Entrada
for i in range(cantidad_notas):
    nota = float(input(f"Ingresa la nota {i+1}: "))
    suma_notas += nota

# Cálculo
promedio = suma_notas / cantidad_notas

# Evaluación y mensaje
if promedio >= 3.0:
    print(f"Promedio: {promedio} -> ¡Aprobaste!")
else:
    print(f"Promedio: {promedio} -> No aprobaste.")