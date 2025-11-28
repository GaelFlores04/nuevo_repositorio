---
title: "Practica 2: Programación Orientada a Objetos"
date: 2025-10-17
categories: ["practicas"]
type: "posts"
author: "Gael Flores Cañedo"
summary: "Reporte sobre la programacion orientada a objetos"
tags: ["Python", "POO", "Programación funcional"]
---

Universidad Autónoma de Baja California 
Facultad de Ingeniería Arquitectura y Diseño 

Ingeniero en computación 
Ingeniero en Software y tecnologías emergentes 

Materia:  Paradigmas de la Programación 

Alumno:  Gael Flores Cañedo 

Matrícula: 376339 

Maestro:  Carlos Gallegos

Practica No.        :   2. 

mailto:gallegosj89@uabc.edu.mx

Universidad Autónoma de Baja California 
Facultad de Ingeniería Arquitectura y Diseño 

Práctica 2: Programación Orientada a Objetos 

1. Conceptos Fundamentales de la Programación Orientada a Objetos 

1. Clase: Una clase es una plantilla o molde que define las características y comportamientos comunes de un conjunto de objetos. En el programa, la clase Book define los atributos y métodos de los libros, mientras que la clase Member define los de los usuarios.  

2. Objeto: Un objeto es una instancia concreta de una clase. Por ejemplo, al ejecutar book = Book(1, '1984', 'Orwell', 1949, Genre.FICTION, 3), se crea un objeto con sus propios valores para cada atributo.  

3. Herencia: Permite crear clases derivadas basadas en otras. En el programa, Book y Magazine heredan de la clase base Item, reutilizando atributos y métodos comunes como el ID, el título y la cantidad disponible.  

4. Encapsulamiento: Consiste en proteger los datos internos de una clase del acceso externo directo. En el código, los atributos comienzan con un guion bajo (por ejemplo, _id, _title), indicando que son de uso interno y deben manipularse a través de métodos. 

5. Abstracción: Consiste en mostrar solo la información esencial y ocultar los detalles internos. Por ejemplo, el usuario solo usa métodos como agregar_item o prestar_item, sin preocuparse por cómo se gestiona internamente la lista de ítems.  

6. Polimorfismo: Permite que diferentes clases respondan al mismo método de distintas formas. Por ejemplo, tanto Book como Magazine implementan el método mostrar_info(), pero cada uno imprime detalles distintos según su tipo.  

2. Comparación entre la versión en C y la versión en Python  

En la versión en C, la biblioteca se implementó usando estructuras (struct) para representar libros y usuarios, junto con funciones independientes para gestionar préstamos, devoluciones y almacenamiento. La memoria debía manejarse manualmente con malloc y free. En cambio, en la versión en Python se utiliza Programación Orientada a Objetos, que permite organizar mejor el código en clases, definir comportamientos mediante métodos y manejar la memoria automáticamente. Además, el manejo de archivos se simplifica gracias a herramientas como JSON. La herencia facilita la extensión del sistema, permitiendo incorporar nuevos tipos de ítems sin reescribir toda la lógica.  

3. Conclusiones sobre las ventajas de la Programación Orientada a Objetos  

●  El POO permite representar mejor los elementos del mundo real mediante clases y objetos.  

●  El código es más fácil de mantener, entender y ampliar.  

●  La herencia y el polimorfismo reducen la duplicación de código.  

●  El encapsulamiento mejora la seguridad y estabilidad del programa.  

●  Python facilita la implementación de POO con menos código y sin necesidad de gestionar manualmente la memoria. 

Universidad Autónoma de Baja California 
Facultad de Ingeniería Arquitectura y Diseño 

En conclusión, la migración del programa de Biblioteca desde C hacia Python demuestra las ventajas prácticas de la POO, ya que se obtiene un sistema más modular, flexible y fácil de extender, sin perder funcionalidad ni eficiencia. 

Referencias 

● Qué es la Programación Orientada a Objetos. (n.d.). Intelequia. 
https://intelequia.com/es/blog/post/qu%C3%A9-es-la-programaci%C3%B3n-orientada-a-objetos 

● Características de la POO. (2021, March 1). Portal Académico Del CCH. 
https://portalacademico.cch.unam.mx/cibernetica1/algoritmos-y-codificacion/caracteristicas-POO 

● Canelo, M. M. (2025, September 1). ¿Qué es la Programación Orientada a Objetos? Profile Software Services. 
https://profile.es/blog/que-es-la-programacion-orientada-a-objetos/
