---
title: "Practica 0:Markdown, Git, GitHub, Hugo y GitHub Actions"
date: 2025-08-15
categories: ["practicas"]
type: "posts"
author: "Gael Flores Cañedo"
summary: "Reporte de Markdown, Git, GitHub, Hugo y GitHub Actions"
tags: ["Haskell", "GHCup", "Instalación", "Hugo","MarkDown"]
---

# **Reporte: Uso de Markdown, Git/GitHub, Hugo y GitHub Actions**
**Autor:** Gael Flores Cañedo  
**Portafolio en GitHub:** [portafolio-PP](https://github.com/GaelFlores04/Portafolio-de-evidencias-Paradigmas)
**Página en GitHub Pages:** [GaelFlores04](https://github.com/GaelFlores04)

---

## **Introducción**

En este reporte presento lo aprendido en las primeras sesiones del curso: Markdown, Git y GitHub, así como la creación de sitios estáticos con Hugo y el despliegue automatizado con GitHub Actions y GitHub Pages. Este documento será la primera entrada en mi portafolio personal.

---

# **1. Markdown**

## ¿Qué es Markdown?

Markdown es un lenguaje de marcado ligero diseñado para crear documentos con formato sin necesidad de usar HTML. Es ampliamente utilizado en documentación, blogs y plataformas como GitHub.

---

## Sintaxis básica de Markdown

### Títulos

# Título 1
## Título 2
### Título 3

### Listas

- Elemento de lista 1
- Elemento de lista 2
* Elemento de lista 3
* Elemento de lista 4
+ Elemento de lista 5
+ Elemento de lista 6

### Listas ordenadas

1. Elemento de lista 1
2.  Elemento de lista 2
    - Elemento de lista 3
    - Elemento de lista 4
        1. Elemento de lista 5
        2. Elemento de lista 6

### Codigos de bloques
~~~
Creando códigos de bloque.
Puedes añadir tantas líneas y párrafos como quieras.  
~~~

### Sintaxis Markdown
En este apartado descubrirás la sintaxis Markdown y los conceptos básicos para escribir utilizando este lenguaje de marcado. De hecho, al final del mismo estarás perfectamente capacitado para empezar a utilizar este lenguaje en tus escritos y publicaciones.



La mejor manera de hacerse una idea de la sintaxis de Markdown es simplemente echar un vistazo a un escrito formateado como tal.

## Título
### Subtítulo
Este es un ejemplo de texto que da entrada a una lista genérica de elementos:
- Elemento 1
- Elemento 2
- Elemento 3
Este es un ejemplo de texto que da entrada a una lista numerada:
1. Elemento 1
2. Elemento 2
3. Elemento 3

Al texto en Markdown puedes añadirle formato como **negrita** o *cursiva* de una manera muy sencilla.
Como ves, se cumple perfectamente uno de los objetivos para los que Markdown fue diseñado, y es hacer las publicaciones lo más legibles posible.

Otro de los objetivos de Markdown, es que puedas publicar los documentos “como están”. No importa si el resultado final que necesitas es HTML, un PDF o texto en formato enriquecido (RTF); ya que siempre podrás obtener estos formatos a través de un conversor, o a través de aplicaciones compatibles con Markdown.

Índice de sintaxis Markdown
En el lenguaje Markdown encontrarás tres tipos de elementos básicos que a su vez engloban el resto de la sintaxis. Considera esto una cheat sheet con la que guiarte.

Elementos de bloque
Párrafos y saltos de línea
Encabezados
Citas
Listas
Códigos de bloque
Reglas horizontales
Elementos de línea
Énfasis
Links o enlaces
Código
Imágenes



Elementos varios
Links automáticos
Omitir Markdown
Elementos de bloque
Párrafos y saltos de línea
Para generar un nuevo párrafo en Markdown simplemente separa el texto mediante una línea en blanco (pulsando dos veces intro)

Al igual que sucede con HTML, Markdown no soporta dobles líneas en blanco, así que si intentas generarlas estas se convertirán en una sola al procesarse.

Para realizar un salto de línea y empezar una frase en una línea siguiente dentro del mismo párrafo, tendrás que pulsar dos veces la barra espaciadora antes de pulsar una vez intro.

Por ejemplo si quisieses escribir un poema Haiku quedaría tal que así:

«Andando con sus patitas mojadas,
el gorrión
por la terraza de madera»

Donde cada verso tiene dos espacios en blanco al final.

Encabezados
Las # almohadillas son uno de los métodos utilizados en Markdown para crear encabezados. Debes usarlos añadiendo uno por cada nivel.

Es decir,

# Encabezado 1
## Encabezado 2
### Encabezado 3
#### Encabezado 4
##### Encabezado 5
###### Encabezado 6

Se corresponde con

Encabezado 1
Encabezado 2
Encabezado 3
Encabezado 4
Encabezado 5
Encabezado 6

También puedes cerrar los encabezados con el mismo número de almohadillas, por ejemplo escribiendo ### Encabezado 3 ###. Pero la única finalidad de esto es un motivo estético.

Existe otra manera de generar encabezados, aunque este método está limitado a dos niveles.

Consiste en subrayar los encabezados con el símbolo = (para el encabezado 1), o con guiones - para el encabezado 2.

Es decir,

Esto sería un encabezado 1
===
Esto sería un encabezado 2
—-
No existe un número concreto = o - que necesites escribir para que esto funcione, ¡incluso bastaría con uno!

Citas
Las citas se generar utilizando el carácter mayor que > al comienzo del bloque de texto.

> Un país, una civilización se puede juzgar por la forma en que trata a sus animales.  — Mahatma Gandhi
Un país, una civilización se puede juzgar por la forma en que trata a sus animales. — Mahatma Gandhi

Si la cita en cuestión se compone de varios párrafos, deberás añadir el mismo símbolo > al comienzo de cada uno de ellos.

> Creo que los animales ven en el hombre un ser igual a ellos que ha perdido de forma extraordinariamente peligrosa el sano intelecto animal.
> Es decir, que ven en él al animal irracional, al animal que ríe, al animal que llora, al animal infeliz. — Friedrich Nietzsche
Creo que los animales ven en el hombre un ser igual a ellos que ha perdido de forma extraordinariamente peligrosa el sano intelecto animal.

Es decir, que ven en él al animal irracional, al animal que ríe, al animal que llora, al animal infeliz. — Friedrich Nietzsche

Incluso puedes concatenar varios >> para crear citas anidadas.

> Esto sería una cita como la que acabas de ver.
> 
> > Dentro de ella puedes anidar otra cita.
> 
> La cita principal llegaría hasta aquí. 
Esto sería una cita como la que acabas de ver.

Dentro de ella puedes anidar otra cita.

La cita principal llegaría hasta aquí.

Recuerda separar los saltos de línea con >, o >> si te encuentras dentro de la cita anidada; para crear párrafos dentro del mismo bloque de cita.

Listas
A diferencia de lo que ocurre en HTML, generar listas en Markdown es tremendamente sencillo. Puedes encontrarte con dos tipos.

Listas desordenadas
Para crear listas desordenadas utiliza * asteriscos, - guiones, o + símbolo de suma.

- Elemento de lista 1
- Elemento de lista 2
* Elemento de lista 3
* Elemento de lista 4
+ Elemento de lista 5
+ Elemento de lista 6

Da igual qué elemento escojas, incluso puedes intercambiarlos. Todos se verán igual al procesarse.

Elemento de lista 1
Elemento de lista 2
Elemento de lista 3
Elemento de lista 4
Elemento de lista 5
Elemento de lista 6
Para generar listas anidadas dentro de otras, simplemente tendrás que añadir **cuatro espacios en blanco antes del siguiente *, - o +.

- Elemento de lista 1
- Elemento de lista 2
    - Elemento de lista 3
    - Elemento de lista 4
        - Elemento de lista 5
        - Elemento de lista 6
Elemento de lista 1
Elemento de lista 2
Elemento de lista 3
Elemento de lista 4
Elemento de lista 5
Elemento de lista 6
Listas ordenadas
Para crear listas ordenadas debes utilizar la sintaxis de tipo: «número.» 1.. Al igual que ocurre con las listas desordenadas, también podrás anidarlas o combinarlas.

1. Elemento de lista 1
2.  Elemento de lista 2
    - Elemento de lista 3
    - Elemento de lista 4
        1. Elemento de lista 5
        2. Elemento de lista 6
Elemento de lista 1
Elemento de lista 2
Elemento de lista 3
Elemento de lista 4
Elemento de lista 5
Elemento de lista 6
Códigos de bloque
Si quieres crear un bloque entero que contenga código. Lo único que tienes que hacer es encerrar dicho párrafo entre dos líneas formadas por tres ~ virgulillas.

Tal que así:




~~~
Creando códigos de bloque.
Puedes añadir tantas líneas y párrafos como quieras.  
~~~
De esta forma, obtendrás el siguiente resultado:

Creando códigos de bloque.
Puedes añadir tantas líneas y párrafos como quieras.
Reglas horizontales
Las reglas horizontales se utilizan para separar secciones de una manera visual. Las estás viendo constantemente en este artículo ya que las estoy utilizando para separar los diferentes elementos de sintaxis de Markdown.

Para crearlas, en una línea en blanco deberás incluir tres de los siguientes elementos: asteriscos, guiones, o guiones bajos.

Es decir

***
---
___
También puedes separarlos mediante un espacio en blanco por pura estética.

* * *
- - -
_ _ _
Elementos de línea
### Énfasis (negritas y cursivas)

*cursiva*	

_cursiva_	

**negrita**	

__negrita__	

***cursiva y negrita***	

___cursiva y negrita___	
---
### Links o enlaces
[enlace en línea](http://www.limni.net)	


### Bloques de código
`Esto es una línea de código`

### Imagenes
![Texto alternativo](/img/ds.jpg)

---

# **2. Git y GitHub**

## ¿Qué es Git?

Git es un sistema de control de versiones que permite registrar cambios y trabajar en equipo sin perder historial.

## ¿Qué es GitHub?

GitHub es una plataforma en línea donde se almacenan repositorios Git y se facilita la colaboración y publicación de proyectos.

---

## Comandos esenciales de Git

```bash
git init
git status
git add .
git commit -m "mensaje"
git branch -M main
git remote add origin URL
git push -u origin main
```

---

# **3. Hugo y GitHub Actions**

## ¿Qué es Hugo?

Hugo es un generador de sitios estáticos extremadamente rápido, basado en Markdown y plantillas.

## ¿Qué es GitHub Actions?

Es una herramienta dentro de GitHub que permite automatizar tareas como compilar sitios y publicarlos automáticamente.

---

## Crear un sitio nuevo en Hugo

```bash
hugo new site mi-sitio
cd mi-sitio
git init
```

---

## Crear una nueva entrada

```bash
hugo new posts/reporte-intro.md
```

---

## Flujo de despliegue automático (GitHub Actions)

Archivo recomendado en:

```
.github/workflows/hugo.yml
```

```yml
name: Deploy Hugo site

on:
  push:
    branches: ["main"]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
        with:
          submodules: true

      - name: Instalar Hugo
        uses: peaceiris/actions-hugo@v2
        with:
          hugo-version: 'latest'

      - name: Construir sitio
        run: hugo --minify

      - name: Deploy a GitHub Pages
        uses: peaceiris/actions-gh-pages@v3
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./public
```

---

## **Conclusión**

Markdown facilita la documentación, Git y GitHub permiten colaboración segura, y Hugo junto con GitHub Actions facilita crear y publicar sitios estáticos profesionales sin necesidad de un servidor propio. Este documento es mi primera entrada en mi portafolio personal.
