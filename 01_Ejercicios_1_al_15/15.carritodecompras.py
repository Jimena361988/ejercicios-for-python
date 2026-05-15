# Total inicial
total_compra = 0.0

# Ingreso de precios
for i in range(5):
    precio = float(input(f"Ingresa precio del producto {i+1}: "))
    total_compra += precio

# Salida final
print("El total a pagar es: $", total_compra)