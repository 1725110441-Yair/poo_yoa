# Repositorio de Programación Orientada a Objetos con Python
Repositorio con ejercicios de Programación Orientada a Objetos
Markdown

## 1. Crear .gitignore 

Crear el archivo .gitignore para configurar los archivos y carpetas no deseamos que se guarden en el repositorio

````shell
*.pyc
__pycache__/
````

## 2. Indexar archivos y carpetas

Indexa todos los directorios y carpetas en busca de documentos nuevos.

````shell
git add .
````

## 3. Crear un COMMIT

Crear un commit o punto de control de los cambios realizados en el proyecto

````shell
git commit -m "CREATED .gitignore"
````

* CREATED - Se crearon nuevas carpetas o archivos.
* UPDATED - Se actualizaron o agregaron nuevas.
* FIXED - Se corrigieron errores.

## 4. Realizar el COMMIT

Sincroniza los cambios realizados en el repositorio.

````shell
git push -u origin main
````

