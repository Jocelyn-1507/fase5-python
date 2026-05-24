# =========================================
# UNIVERSIDAD NACIONAL ABIERTA Y A DISTANCIA
# Curso: Fundamentos de Programacion
# Fase 5 - Evaluacion Final POA
#
# Estudiante: Jocelyn Delgado Tamayo
# Fecha: 2026-05-26
# Grupo: 680
#
# Problema 2:
# Gestion de precios de un menu de restaurante
# =========================================

# MATRIZ DE PRODUCTOS
# [Nombre, Categoria, Precio Base]

menu = [
    ["Hamburguesa", "Comida rapida", 25000],
    ["Pizza", "Comida rapida", 30000],
    ["Ensalada", "Saludable", 18000],
    ["Jugo Natural", "Bebidas", 12000],
    ["Pasta", "Italiana", 28000],
    ["Cafe", "Bebidas", 8000]
]

# CATEGORÍA OBJETIVO
categoria_objetivo = "Comida rapida"

# UMBRAL MÍNIMO
umbral = 20000


# FUNCIÓN PARA CALCULAR EL PRECIO FINAL
def calcular_precio_final(categoria, precio):

    # Verificar si cumple las condiciones
    if categoria == categoria_objetivo and precio > umbral:

        # Aplicar descuento del 15%
        descuento = precio * 0.15

        # Calcular precio final
        precio_final = precio - descuento

    else:
        # Mantener el precio original
        precio_final = precio

    return precio_final


# MOSTRAR RESULTADOS
print("\n===== MENU DEL RESTAURANTE =====\n")

for producto in menu:

    nombre = producto[0]
    categoria = producto[1]
    precio_base = producto[2]

    # Llamado de la función
    precio_final = calcular_precio_final(categoria, precio_base)

    # Mostrar información
    print(f"Producto: {nombre}")
    print(f"Categoria: {categoria}")
    print(f"Precio base: ${precio_base}")
    print(f"Precio final: ${precio_final:.0f}")
    print("-----------------------------------")