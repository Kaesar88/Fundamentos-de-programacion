import time

# =================================================================
# MÓDULO 1: CLASES, ESTRUCTURAS DE DATOS Y LÓGICA DE NEGOCIO
# CUMPLIMIENTO: Diseño Orientado a Objetos (OOD) y Estructuras Básicas
# =================================================================

class Producto:
    """
    Clase que representa un producto en el inventario, encapsulando
    sus atributos y proporcionando métodos para su gestión.
    (Integra el Fragmento de Código de Clase del Anexo - Ejemplo 1)
    """
    # Atributos: nombre (str), precio (float), cantidad (int), id (int)
    
    def __init__(self, id_producto: int, nombre: str, precio: float, cantidad: int):
        self.id = id_producto
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        """Representación legible del objeto Producto."""
        # Se asegura un formato de impresión limpio y alineado para la UI de consola.
        return f"ID: {self.id:<3} | Nombre: {self.nombre:<15} | Precio: ${self.precio:7.2f} | Cantidad: {self.cantidad:4d}"

# Estructura de datos principal (Lista de objetos Producto)
inventario = [
    Producto(1, "Camiseta", 20.0, 50),
    Producto(2, "Pantalones", 40.0, 30),
    # Corrección en el precio del zapato según la imagen de ejemplo (60.0), aunque tu código tenía 168.0
    Producto(3, "Zapatos", 60.0, 20) 
]

# Variable Global (Alcance): Contador para asignar IDs de forma única
siguiente_id = 4
# Variable Constante (Datos Cuantitativos del Caso)
TASA_ERROR_INVENTARIO_PREVIO = 0.15 # 15% de error mencionado en el contexto.

# =================================================================
# MÓDULO 2: INTEGRACIÓN DEL FRAGMENTO DEL ANEXO Y FUNCIONALIDADES
# =================================================================

def calcular_total_anexo(productos: list) -> float:
    """
    *** FUNCIÓN INTEGRADA DIRECTAMENTE DEL ANEXO (Ejemplo 2) ***
    Calcula el total del inventario en términos de valor monetario.
    
    NOTA: Esta versión opera sobre una lista de diccionarios, no objetos. 
    Se incluye para cumplir el requisito de integración literal.
    
    Args:
    productos (list): Una lista de diccionarios, donde cada diccionario representa
    un producto con las claves 'nombre', 'precio' y 'cantidad'.

    Returns:
    float: El valor total del inventario.
    """
    total = 0.0
    for producto in productos:
        # Nota: La sintaxis de suma es '+=' o 'total = total + ...'
        # El fragmento del anexo usaba '+-', que se corrige a '+=' para que sea funcional
        total += producto['precio'] * producto['cantidad'] 
    return total

def calcular_total_oo(productos: list) -> float:
    """
    Calcula el total del inventario usando la estructura de Objetos (mejor práctica DOO).
    """
    total = 0.0
    # Recorrido (Iteración)
    for producto in productos:
        total += producto.precio * producto.cantidad
    return total

def mostrar_inventario():
    """Recorrido y visualización de la estructura de datos (UI/UX)."""
    print("\n" + "="*50)
    print("         SISTEMA DE CONTROL DE INVENTARIOS")
    print("               INVENTARIO ACTUAL")
    print("="*50)
    print("ID  | Nombre              | Precio ($) | Cantidad")
    print("-" * 50)
    
    # Comprobación de lista vacía
    if not inventario:
        print("El inventario está vacío.")
        print("-" * 50)
        return

    for producto in inventario:
        print(producto)
        
    print("-" * 50)
    valor_total = calcular_total_oo(inventario)
    print(f"VALOR TOTAL (DOO): ${valor_total:,.2f}")
    
    # Dato Cualitativo (Manejo de la problemática inicial)
    print(f"(*) Tasa de error previa: {TASA_ERROR_INVENTARIO_PREVIO*100:.0f}% (Reducida drásticamente con el nuevo sistema).")
    print("="*50)

def agregar_producto():
    """Inserción de un nuevo producto en la estructura de datos."""
    global siguiente_id
    print("\n" + "="*30)
    print("     AGREGAR NUEVO PRODUCTO")
    print("="*30)
    
    # Manejo básico de tipos de datos y errores
    try:
        nombre = input("Ingrese el nombre del producto: ").strip()
        # Uso del tipo float/int, tal como lo requiere la estructura de datos
        precio = float(input("Ingrese el precio del producto: ")) 
        cantidad = int(input("Ingrese la cantidad del producto: "))
        
        if precio <= 0 or cantidad <= 0:
            print("Error: El precio y la cantidad deben ser valores positivos.")
            return
            
    except ValueError:
        print("Error: Entrada inválida para precio o cantidad. Asegúrese de ingresar números.")
        return
    
    # Inserción
    nuevo_producto = Producto(siguiente_id, nombre, precio, cantidad)
    inventario.append(nuevo_producto)
    siguiente_id += 1
    
    print("\nProducto agregado exitosamente.")

def actualizar_cantidad():
    """Búsqueda y modificación de datos."""
    print("\n" + "="*40)
    print("    ACTUALIZAR CANTIDAD DE PRODUCTO")
    print("="*40)
    
    try:
        id_buscar = int(input("Ingrese el ID del producto a actualizar: "))
        nueva_cantidad = int(input("Ingrese la nueva cantidad: "))
        
        if nueva_cantidad < 0:
            print("Error: La cantidad no puede ser negativa.")
            return
            
    except ValueError:
        print("Error: Entrada inválida para el ID o la cantidad.")
        return
    
    # Búsqueda
    for producto in inventario:
        if producto.id == id_buscar:
            producto.cantidad = nueva_cantidad  # Modificación de datos
            print("\nCantidad actualizada exitosamente.")
            return

    print(f"\nError: No se encontró un producto con el ID {id_buscar}.")

def eliminar_producto():
    """Búsqueda y eliminación de datos."""
    print("\n" + "="*30)
    print("      ELIMINAR PRODUCTO")
    print("="*30)
    
    try:
        id_eliminar = int(input("Ingrese el ID del producto a eliminar: "))
    except ValueError:
        print("Error: Entrada inválida para el ID.")
        return

    # Búsqueda e Eliminación
    for i, producto in enumerate(inventario):
        if producto.id == id_eliminar:
            del inventario[i]
            print("\nProducto eliminado exitosamente.")
            return

    print(f"\nError: No se encontró un producto con el ID {id_eliminar}.")

# =================================================================
# MÓDULO 3: INTERFAZ DE USUARIO (UI/UX) Y CONTROL PRINCIPAL
# CUMPLIMIENTO: Integración del Fragmento de Menú y Navegabilidad (Ejemplo 3)
# =================================================================

def mostrar_menu():
    """Muestra el menú principal de la UI/UX."""
    print("\n" + "#"*40)
    print("  SISTEMA DE CONTROL DE INVENTARIOS")
    print("#"*40)
    print("1. Ver Inventario")
    print("2. Agregar Producto")
    print("3. Actualizar Cantidad de Producto")
    print("4. Eliminar Producto")
    print("5. Salir")
    print("-" * 40)

def main():
    """Función principal para el control del programa."""
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == '1':
            mostrar_inventario()
        elif opcion == '2':
            agregar_producto()
        elif opcion == '3':
            actualizar_cantidad()
        elif opcion == '4':
            eliminar_producto()
        elif opcion == '5':
            print("\nSaliendo del sistema. ¡Hasta pronto!")
            break
        else:
            print("\nOpción no válida. Inténtelo de nuevo.")
            
        # Espera para UX: Presione Enter para volver al menú principal
        if opcion in ['1', '2', '3', '4']:
            input("\nPresione Enter para volver al menú principal.")

if __name__ == "__main__":
    main()
