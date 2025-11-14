---
title: "Práctica 1: Markdown, Git, Hugo y GitHub Actions"
date: 2025-11-14
draft: false
---


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

## 3.3 Cómo crear un sitio estático con Hugo
Instalar Hugo

Descargar desde: https://gohugo.io

Crear un nuevo sitio
hugo new site mi-sitio

Agregar un tema
git submodule add URL-del-tema themes/nombreDelTema


En hugo.toml:

theme = "nombreDelTema"

Crear una nueva página
hugo new posts/reporte-practica1.md

Ajustar contenido en Markdown

Escribes tu entrada en el archivo creado.

Construir sitio localmente
hugo server -D

## 3.4 Subir el sitio a GitHub

Inicializar Git en la carpeta del sitio

Conectar con un repositorio

Hacer push:

git add .
git commit -m "Sitio Hugo"
git push -u origin main

## 3.5 Configurar GitHub Actions para publicar en Pages

Crear archivo:

.github/workflows/hugo.yml


Contenido:

name: Deploy Hugo site

on:
  push:
    branches:
      - main

jobs:
  build-deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v3
        with:
          submodules: true
          fetch-depth: 0

      - name: Setup Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'

      - name: Build
        run: hugo --minify

      - name: Deploy
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public


Después en GitHub:

Settings → Pages → "gh-pages" branch
Y tu sitio queda publicado.