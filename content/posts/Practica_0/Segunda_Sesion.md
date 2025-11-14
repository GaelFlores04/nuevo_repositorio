---
title: "Práctica 1: Markdown, Git, Hugo y GitHub Actions"
date: 2025-11-14
draft: false
---


## 2. Uso de Git y GitHub
2.1 ¿Qué es Git?

Git es un sistema de control de versiones que permite guardar el historial completo de un proyecto, trabajar en equipo, y manejar cambios de forma ordenada y segura.

2.2 ¿Qué es GitHub?

GitHub es una plataforma que almacena repositorios Git en la nube, permitiendo:

Respaldo del código

Colaboración

Publicación de proyectos

Uso de GitHub Pages y GitHub Actions

## 2.3 Comandos esenciales de Git
Inicializar repositorio
git init

Configurar usuario
git config --global user.name "Tu Nombre"
git config --global user.email "correo@example.com"

Agregar archivos
git add .

Crear un commit
git commit -m "Mensaje"

Ver estado
git status

Conectar repositorio local con GitHub
git remote add origin https://github.com/usuario/repositorio.git

Subir cambios
git push -u origin main

## 2.4 Cómo crear un repositorio en GitHub

Ir a https://github.com

Clic en New Repository

Dar nombre al proyecto

Crear el repositorio vacío

Conectar con tu carpeta local usando los comandos anteriores

## 3. Generación de páginas estáticas con Hugo y GitHub Actions
3.1 ¿Qué es Hugo?

Hugo es un generador de sitios estáticos extremadamente rápido.
Permite crear blogs, portafolios, documentación y páginas sin usar bases de datos.

Ventajas:

Muy rápido

Basado en Markdown

Fácil de mantener

Ideal para GitHub Pages

3.2 ¿Qué es GitHub Actions?

GitHub Actions es un sistema de automatización integrado en GitHub.
Permite ejecutar tareas automáticamente, como:

Construir tu sitio Hugo

Compilar código

Publicar tu página en GitHub Pages