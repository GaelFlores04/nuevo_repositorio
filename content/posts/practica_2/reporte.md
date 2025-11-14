---
title: "Práctica 2: Migración de Biblioteca (C → Python OOP)"
date: 2025-11-14
draft: false
---

# Reporte de Practica: Migración de Biblioteca de C a Python (POO)

## Objetivo
Migrar el programa de Biblioteca originalmente escrito en C (con estructuras) hacia una versión en Python usando Programación Orientada a Objetos (POO). Implementar clases para Biblioteca, Usuarios e Ítems (libros, revistas) e incluir herencia, encapsulamiento, abstracción y polimorfismo. Además implementar persistencia sencilla (JSON), búsquedas, préstamos y devoluciones.

---

## 1. Diseño orientado a objetos (resumen)
Se definieron las siguientes clases:
- `Item` (abstracta): define comportamiento común (id, título, año, estado).
- `Book` y `Magazine`: subclases de `Item` (herencia).
- `User`: representa usuarios con lista de ítems prestados.
- `Library`: gestor que mantiene colecciones, persiste en JSON y ofrece operaciones.

### Ejemplo de código (fragmento)
```python
class Book(Item):
    def item_type(self): return "book"
    def __init__(self, item_id, title, author, year, isbn=None):
        super().__init__(item_id, title, year)
        self.author = author
2. Explicación de conceptos POO con ejemplos
Clase y Objeto
Clase: plantilla (por ejemplo Book).

Objeto: instancia de la clase: b = Book("b001", "Estructuras", "Autor", 2010).

Herencia
Book hereda de Item, reutiliza atributos y métodos.

Encapsulamiento
Atributos como _id son privados/protegidos; acceso controlado mediante propiedades o métodos.

Abstracción
Item define la interfaz mínima (métodos borrow, give_back, to_dict) que es usada por Library.

Polimorfismo
Library llama to_dict() o item_type() sin conocer la subclase exacta (libro o revista).

3. Funcionalidad implementada
Registrar usuarios e ítems (libros/revistas).

Buscar ítems por título, autor o tipo.

Prestar y devolver ítems (validaciones: disponibilidad, quien presta).

Persistencia en biblioteca_data.json.

Menú de consola simple para interacción.

4. Comparación C vs Python (breve)
Estructuras en C: el programa original gestionaba structs, arrays y funciones globales para operaciones. La manipulación de memoria y manejo de cadenas era explícita y propensa a errores.

POO en Python: organiza el código en tipos (clases), mejora la modularidad y legibilidad. Python ofrece manejo automático de memoria (garbage collector) y JSON para persistencia de forma fácil.

Ventajas de Python/POO:

Mayor abstracción y reutilización (herencia).

Menos código «ceremonial»: no hay punteros/dereferencias explícitas.

Más seguro frente a errores de memoria.

Desventajas:

Menor control fino sobre memoria y performance frente a C.

Requiere traducción lógica (no es un copy/paste).

5. Conclusiones
La migración a POO mejora la estructura del código, facilita la extensión (añadir nuevos tipos de ítems), y reduce errores comunes de manejo de memoria. Para aplicaciones didácticas y prototipos, Python ofrece un ciclo de desarrollo más rápido y un código más mantenible.