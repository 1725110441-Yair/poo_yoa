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

## 5. Agregar Documentación a los métodos

Agregar un **Docstring** a los métodos generados.

````python
"""
--------------------------

# Aqui va la descripcion de sobre lo que hace el metodo.

--------------------------

# (Aqui estan los argumentos con descripción.)
Args: 
variable_uno : int - Primer numero entero
variable_dos : int - Segundo numero entero

--------------------------

# (Aqui es lo que regresa el codigo con descripción.)
Return: 
suma : int - Suma de los numeros enteros

--------------------------
"""
````