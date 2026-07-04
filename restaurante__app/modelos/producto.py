class Producto:
    def __init__(self, nombre, precio, disponibilidad):
        self.nombre = nombre
        self.__precio = 0.0
        self.cambiar_precio(precio)
        self.disponibilidad = disponibilidad

    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.__precio = nuevo_precio
        else:
            print(f"Error: El precio de '{self.nombre}' debe ser mayor que 0.")

    def obtener_precio(self):
        return self.__precio

    def mostrar_informacion(self):
        estado = "Disponible" if self.disponibilidad else "No disponible"
        return f"Producto: {self.nombre} | Precio: ${self.obtener_precio():.2f} | Estado: {estado}"

    def __str__(self):
        return self.mostrar_informacion()