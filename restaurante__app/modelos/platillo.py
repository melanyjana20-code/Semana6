from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, disponibilidad, calorias, tiempo_preparacion):
        super().__init__(nombre, precio, disponibilidad)
        self.calorias = calorias
        self.tiempo_preparacion = tiempo_preparacion

    def mostrar_informacion(self):
        info_padre = super().mostrar_informacion()
        return f"{info_padre} | Calorías: {self.calorias} kcal | Preparación: {self.tiempo_preparacion} min"