from modelos.producto import Producto

class Restaurante:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
            print(f"Registrado con éxito: {producto.nombre}")
        else:
            print("Error: Solo se pueden agregar instancias de Producto.")

    def mostrar_menu(self):
        print("\n--- Menú del Restaurante ---")
        for producto in self.productos:
            print(producto.mostrar_informacion())
        print("-------------------------------\n")