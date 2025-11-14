---
title: "Práctica 1: Práctica 1: Elementos básicos de los lenguajes de programación"
date: 2025-11-14
draft: false
---



# Práctica: Elementos Fundamentales de los Lenguajes de Programación

## **1. Introducción**
El objetivo de esta práctica es identificar los elementos fundamentales de los lenguajes de programación dentro de la aplicación propuesta. Estos elementos permiten comprender cómo funcionan los programas a nivel interno, cómo se organiza la memoria, cómo se gestionan las funciones y cómo se ejecutan las instrucciones.

Además, este reporte forma parte del portafolio y debe ser integrado como la **segunda entrada** del sitio estático generado con Hugo.

En este documento se analizan los siguientes conceptos:
- Nombres
- Marcos de activación
- Bloques de alcance
- Administración de memoria
- Expresiones
- Comandos
- Control de secuencia: selección, iteración y recursión
- Subprogramas
- Tipos de datos

Finalmente, se da evidencia de estos conceptos dentro del repositorio propuesto.

Repositorio analizado: **https://github.com/gallegosj89/portafolio**

---

## **2. Elementos Fundamentales en Lenguajes de Programación**

### **2.1 Nombres**
Los *nombres* son identificadores utilizados para referirse a variables, funciones, clases o elementos del programa. En la aplicación del repositorio se pueden observar nombres utilizados para:
- Variables utilizadas para almacenar datos.
- Funciones definidas para modular el código.
- Archivos y módulos que representan componentes del sistema.

**Ejemplo típico:**
```python
title = "Mi Portafolio"
```

---

### **2.2 Marcos de Activación (Activation Records)**
Los marcos de activación son estructuras que se crean en la pila (stack) cuando una función es llamada. Contienen:
- Parámetros
- Variables locales
- Dirección de retorno

En la aplicación, cada vez que se ejecuta una función, el lenguaje (Python/JavaScript, según corresponda) adminstra automáticamente estos marcos.

**Ejemplo conceptual:**
```python
def procesar_datos(x):
    y = x + 2
    return y
```
Cada llamada crea un marco con el valor de `x`, `y` y la dirección de retorno.

---

### **2.3 Bloques de Alcance (Scope Blocks)**
El *alcance* define dónde una variable es accesible.

Existen dos tipos principales:
- **Alcance local** (dentro de funciones)
- **Alcance global** (fuera de funciones)

**Ejemplo:**
```python
contador = 0  # global

def incrementar():
    local = 1  # local
    return contador + local
```

---

### **2.4 Administración de Memoria**
La memoria se divide en:
- **Heap**: objetos creados dinámicamente
- **Stack**: marco de activación

El lenguaje utilizado en el repositorio administra la memoria automáticamente (garbage collector). Por ejemplo, al crear estructuras, listas u objetos, estos se almacenan en memoria dinámica y se liberan al ya no usarse.

**Ejemplo:**
```python
datos = [1, 2, 3]  # almacenado en heap
```

---

### **2.5 Expresiones**
Una expresión es una combinación de operadores y operandos que produce un valor.

**Ejemplos típicos encontrados:**
```python
x = a + b
condicion = edad >= 18
```

---

### **2.6 Comandos (Statements)**
Los comandos modifican el estado del programa e incluyen:
- Asignaciones
- Llamadas a funciones
- Estructuras de control

**Ejemplo:**
```python
mensaje = "Hola"
print(mensaje)
```

---

### **2.7 Control de Secuencia**

#### **a) Selección**
Estructuras como `if`, `elif`, `else`.
```python
if edad >= 18:
    print("Adulto")
```

#### **b) Iteración**
Uso de ciclos como `for` y `while`.
```python
for i in range(5):
    print(i)
```

#### **c) Recursión**
Una función que se llama a sí misma.
```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)
```

---

### **2.8 Subprogramas**
Son funciones o procedimientos diseñados para modularizar el programa.

En el repositorio se evidencian funciones empleadas para:
- Procesar datos
- Organizar componentes
- Realizar validaciones

**Ejemplo:**
```python
def generar_reporte():
    pass
```

---

### **2.9 Tipos de Datos**
Un lenguaje puede manejar diferentes tipos como:
- Enteros (int)
- Flotantes (float)
- Cadenas (string)
- Listas, tuplas o estructuras

**Ejemplo:**
```python
numero = 10
mensaje = "Hola"
lista = [1,2,3]
```

---

## **3. Identificación de Conceptos en la Aplicación del Repositorio**
Dentro del repositorio proporcionado se identifican todos los conceptos previos mediante:
- Funciones definidas en los módulos del proyecto
- Lógica para procesar datos y generar salidas
- Estructuras de control usadas para flujo del programa
- Tipos de datos utilizados para manejar información
- Alcance y administración de memoria implícita

Cada archivo del repositorio aplica estos elementos de forma práctica.

---

## **4. Enlaces Requeridos**
- **Repositorio del portafolio:** https://github.com/gallegosj89/portafolio

---

## **5. Conclusiones**
Esta práctica permite comprender cómo los conceptos fundamentales de los lenguajes de programación se reflejan en programas reales. Analizar estos elementos ayuda a mejorar la comprensión del funcionamiento interno de los lenguajes, la ejecución del código y la estructura de los programas.
