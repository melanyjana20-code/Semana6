from modelos.producto import Producto
from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante


def ejecutar_restaurante():
    # Crear restaurante
    mi_restaurante = Restaurante()

    # Crear productos
    platillo1 = Platillo("Tacos al Pastor", 50.0, True, 300, 15)
    platillo2 = Platillo("Salmón a la Parrilla", 60.0, True, 400, 20)
    bebida1 = Bebida("Coca-Cola", 20.0, True, 500, "Refresco")
    souvenir = Producto("Gorra Oficial del Restaurante", 15.0, True)

    # Agregar productos al restaurante
    mi_restaurante.agregar_producto(platillo1)
    mi_restaurante.agregar_producto(platillo2)
    mi_restaurante.agregar_producto(bebida1)
    mi_restaurante.agregar_producto(souvenir)

    # Mostrar inventario
    print("----- INVENTARIO DEL RESTAURANTE -----")
    mi_restaurante.mostrar_menu()


if __name__ == "__main__":
    ejecutar_restaurante()