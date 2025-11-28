---
title: "Practica 1:Elementos básicos de los lenguajes de programación"
date: 2025-09-20
categories: ["practicas"]
type: "posts"
author: "Gael Flores Cañedo"
summary: "Git, GitHub, Hugo y GitHub Actions"
tags: ["Haskell", "GHCup", "Instalación", "Hugo","MarkDown"]
---

# Práctica – Elementos Básicos de los Lenguajes de Programación

Este reporte resume y explica los **nueve elementos fundamentales** que componen cualquier lenguaje de programación, basándose en el documento proporcionado.

---

## 1. **Nombres (Identificadores)**

Los identificadores son los nombres que se asignan a entidades dentro de un programa, tales como:

- **Variables globales**: `static_var`, `bss_var`, `heap_allocations`, `stack_allocations`
- **Variables locales**: `library`, `members`, `bookCount`, `memberCount`, `choice`
- **Funciones**: `addBook`, `issueBook`, `freeLibrary`, `displayMemoryUsage`
- **Tipos definidos por el programador**: `book_t`, `member_t`, `genre_t`

---

## 2. **Marcos de Activación (Activation Records / Stack Frames)**

Cada vez que se llama una función, se crea un **marco de activación en el stack**, el cual contiene parámetros, variables locales, dirección de retorno y espacio temporal para cálculos.

Ejemplo en la función `addBook(&library, &bookCount)`.

---

## 3. **Bloques de Alcance (Scope)**

Determinan dónde es válido un nombre:

- Alcance global: variables globales, funciones, tipos.
- Alcance local: variables dentro de funciones.
- Alcance dentro de estructuras de control: cada `if`, `while`, `for` crea un bloque nuevo.

---

## 4. **Administración de Memoria**

Los programas manejan memoria en distintos segmentos:

### Estática
```c
static int static_var = 0;
```

### BSS
```c
int bss_var;
```

### Automática (Stack)
```c
int choice, bookCount;
```

### Dinámica (Heap)
Uso de `malloc`, `realloc`, `free` en funciones como:
- `addBook`
- `addMember`
- `issueBook`
- `freeLibrary`

---

## 5. **Expresiones**

Ejemplos:
- `new_book->id = 10;`
- `memberFound->issued_count * sizeof(int);`
- `if (current->id == bookID)`

---

## 6. **Comandos**

Acciones como:
- Entrada/salida (`printf`, `scanf`)
- Asignaciones (`=`)
- Llamadas a funciones (`addBook()`)
- Manejo de archivos (`fopen`, `fprintf`)

---

## 7. **Control de Secuencia**

Incluye:

### Selección
```c
if (...) { ... }
switch (choice)
```

### Iteración
```c
while (current)
for (int i = 0; i < issued_count; i++)
```

### Recursión
```c
displayBooksRecursive(book_t *library)
```

---

## 8. **Subprogramas (Funciones)**

### Definidas por el programador:
- `addBook`
- `issueBook`
- `displayBooks`
- `saveLibraryToFile`

### Librerías del sistema:
- `malloc`
- `free`
- `printf`
- `fopen`

---

## 9. **Tipos de Datos**

Incluye:

- **Primitivos:** `int`, `char`, `size_t`
- **Compuestos (`struct`):**
```c
struct book_t { ... };
```
- **Enumerados:** `genre_t`
- **Apuntadores:** `book_t *library`
- **Arreglos:** `char title[100]`

---

# Conclusión

Esta práctica permite reconocer los elementos fundamentales que componen cualquier lenguaje de programación. Conocer sus estructuras, manejo de memoria, control de flujo y tipos de datos ayuda a escribir programas más claros, seguros y eficientes.
