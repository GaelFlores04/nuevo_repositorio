---
title: "Practica 3:Instalación del entorno de desarrollo Haskell"
date: 2025-11-07
categories: ["practicas"]
type: "posts"
author: "Gael Flores Cañedo"
summary: "Reporte sobre la instalación del entorno de desarrollo Haskell utilizando GHCup, y análisis de la aplicación TODO en Haskell."
tags: ["Haskell", "GHCup", "Instalación", "Programación funcional"]
---

# Instalación del entorno de desarrollo Haskell

## Introducción

Haskell es un lenguaje de programación **puramente funcional** que se destaca por su elegancia, tipado fuerte y capacidad de abstracción.  
Aunque no es tan popular como C o Python, es ampliamente utilizado en ámbitos académicos y en el desarrollo de software confiable.  
El objetivo de esta práctica es **instalar el entorno de desarrollo de Haskell** y analizar el funcionamiento de la aplicación **TODO**, la cual sirve como ejemplo introductorio al uso de este lenguaje.

---

## 1. Instalación del entorno de Haskell con GHCup

### 1.1. Descarga e instalación de GHCup

El primer paso consiste en acceder a la página oficial de descargas de Haskell, donde se indica que todas las herramientas pueden instalarse mediante **GHCup**.  
Para sistemas Windows, el proceso se realiza desde **PowerShell (sin modo administrador)** con el siguiente comando:

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force; iex ((New-Object System.Net.WebClient).DownloadString('https://get-ghcup.haskell.org'))
```

Este comando descarga e instala **GHCup**, una herramienta que gestiona el entorno de Haskell y permite instalar, actualizar o eliminar componentes como GHC, Cabal y Stack.

---

### 1.2. Componentes instalados

Durante la instalación, se agregan las siguientes herramientas:

- **GHCup** → Herramienta principal de instalación y gestión del entorno.  
- **GHC (Glasgow Haskell Compiler)** → Compilador oficial de Haskell.  
- **HLS (Haskell Language Server)** → Proporciona soporte para editores y autocompletado.  
- **Stack** → Manejador de proyectos y dependencias, similar a *pip* en Python.  
- **Cabal** → Herramienta de construcción de proyectos (build tool).  
- **Hugs** → Intérprete interactivo de Haskell (opcional).  

Los archivos de código fuente de Haskell utilizan la extensión `.hs`.

---

### 1.3. Verificación de la instalación

Una vez completada la instalación, se recomienda abrir una nueva terminal y verificar las versiones de las herramientas con los siguientes comandos:

```bash
ghc --version
stack --version
cabal --version
```

Si las versiones aparecen correctamente, el entorno de Haskell está configurado con éxito.

---

## 2. Aplicación TODO en Haskell

### 2.1. Descripción general

La aplicación **TODO** es un ejemplo práctico desarrollado en Haskell que demuestra cómo crear una aplicación de lista de tareas desde la línea de comandos.  
Está basada en un tutorial del blog oficial de Haskell:  
> *"How to use Haskell to build a TODO app with Stack."*

El propósito es mostrar cómo Haskell puede manejar operaciones de entrada/salida y persistencia de datos mediante funciones puras y tipos definidos.

---

### 2.2. Estructura del proyecto

Al crear un nuevo proyecto con Stack, se utiliza el siguiente comando:

```bash
stack new todo-app
cd todo-app
stack setup
stack build
```

La estructura generada contiene los archivos principales:

```
todo-app/
├── app/
│   └── Main.hs
├── src/
│   └── Todo.hs
├── todo-app.cabal
└── stack.yaml
```

El archivo `Main.hs` contiene el punto de entrada del programa, mientras que `Todo.hs` define las funciones de manejo de tareas (agregar, listar y eliminar).

---

### 2.3. Ejecución de la aplicación

Para ejecutar el programa, se utiliza:

```bash
stack run
```

El usuario puede interactuar con la aplicación agregando tareas o listándolas, por ejemplo:

```
1. Agregar tarea
2. Ver tareas
3. Eliminar tarea
4. Salir
```

Las tareas se almacenan en un archivo de texto, demostrando la gestión de archivos y funciones puras en Haskell.

---

## 3. Conclusión

La instalación del entorno de Haskell mediante **GHCup** es un proceso automatizado y sencillo que permite disponer rápidamente de las herramientas necesarias para desarrollar en este lenguaje.  
Haskell, aunque tiene una sintaxis y un paradigma distintos a lenguajes imperativos como C o Python, ofrece una gran potencia expresiva y robustez.

La aplicación **TODO** sirve como un excelente punto de partida para entender cómo los conceptos funcionales (como la inmutabilidad y la composición de funciones) se aplican en proyectos reales.  
En conclusión, esta práctica proporciona una visión introductoria al paradigma funcional y al ecosistema de Haskell, promoviendo una forma diferente y más matemática de pensar la programación.

---

**Autor:** Gael Flores Cañedo  
**Matrícula:** 376339  
**Universidad Autónoma de Baja California (UABC)**  
**Materia:** Paradigmas de la Programación
