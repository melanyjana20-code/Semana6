from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, disponibilidad, volumen_ml, tipo):
        super().__init__(nombre, precio, disponibilidad)
        self.volumen_ml = volumen_ml
        self.tipo = tipo

    def mostrar_informacion(self):
        info = super().mostrar_informacion()
        return f"{info} | Volumen: {self.volumen_ml} ml | Tipo: {self.tipo}"

    def __str__(self):
        return self.mostrar_informacion()