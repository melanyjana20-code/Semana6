# **SISTEMA DE GESTIÓN DE RESTAURANTE**

**Estudiante**

**Nombre completo:** Melany Mercedes Jaña Sambrano

  

## Descripción del sistema

Este sistema es una aplicación desarrollada en Python bajo el paradigma de Programación Orientada a Objetos (POO). Permite gestionar productos de un restaurante como platillos, bebidas y productos generales. El sistema está estructurado de forma modular, separando responsabilidades en modelos (clases) y servicios (lógica del sistema) lo que facilita su mantenimiento, escalabilidad y reutilización del código.

  

## Estructura del proyecto
**Repositorio GitHub**
```text

│ ├── modelos/

│ │ ├── init .py

│ │ ├── producto.py

│ │ ├── platillo.py

│ │ └── bebidapy

│ ├── servicios/

│ │ ├── init .py

│ │ └── restaurante.py

│ └── main.py

└── README.md

```

## Relación de herencia

Se implementa herencia simple donde la clase base es Producto la cual contiene atributos generales como nombre, precio y disponibilidad. 
De esta clase se derivan:

 - Platillo
 - Bebida

Estas clases heredan atributos y métodos de Producto, permitiendo la reutilización de código y especialización de comportamiento.

  
## Atributo encapsulado

El atributo encapsulado es:

 - __precio(en la clase Producto)

Este atributo no puede ser accedido directamente desde fuera de la clase. Su manipulación se realiza mediante métodos como:

 - cambiar_precio()
 - obtener_precio()

Esto garantiza control y seguridad sobre los datos.

  
Polimorfismo aplicado

El polimorfismo se evidencia mediante el método:

 - mostrar_informacion()

Este método está escrito en las clases Platillo y Bebida, permitiendo que cada clase muestre su información de manera diferente según sus propios atributos adicionales.

## Reflexión

La Programación Orientada a Objetos es fundamental en el desarrollo de software moderno ya que estructura permite el código en entidades reutilizables y organizadas. En este proyecto su aplicación facilitó la creación de un sistema modular mejorando la claridad del código, la reutilización de clases y la facilidad de mantenimiento. Además el uso de herencia, encapsulamiento y polimorfismo permitió modelar de manera más realista el funcionamiento de un sistema de restaurante.