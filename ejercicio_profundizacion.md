# Ejercicios de profundización [Python]
EL propósito de este ejercicio es que el alumno ponga sus habilidades de SQL junto con otras adqueridas a lo largo de la carrera como el manejo de archivos CSV. Este es un caso típico de ETL en donde se transforma un sistema legacy de datos (un archivo) en una base de datos.

# Enunciado
El objetivo es realizar un ejercicio muy similar al de "ejercicios_clase" pero ahora el alumno será quien genere clases de la base de datos para construirla.\

Deberá generar una base de datos de libros basada en los archivo CSV libreria_autor.csv y libreria_libro.csv, los cuales poseen las siguientes clase:\
Clase Autor:
- id del autor (id) --> número (clave primaria, autoincremental)
- Nombre del autor (name) --> texto

Clase Libro:
- id del libro (id) --> número (clave primaria, autoincremental)
- Título del libro (title) --> texto
- Cantidad de páginas (pags) --> número
- id del autor (author_id) --> número (clave foránea)
- Objecto autor (author) --> objeto relación (relationship)

## create_schema
Deben crear una función "create_schema" la cual se encargará de crear la base de datos y la tabla correspondiente al esquema definido. Deben usar la sentencia CREATE para crear la tabla mencionada.\
IMPORTANTE: Recuerden que es recomendable para estos ejercicios que se borre toda la base de datos al llamar a create_schema

## fill()
Deben crear una función "fill" que lea los datos de los archivos CSV y cargue esas filas de los archivos como datos de las tablas SQL. Pueden resolverlo de la forma que mejor crean. Recordatorio, primero crear los autores y luego los libros.

## fetch(id)
Deben crear una función que imprima en pantalla los resultados de la tabla "libro", pueden usar esta función para ver que "fill" realizó exactamente lo que era esperado. 
- En caso de que el id sea igual a cero (id=0) deben imprimir todos los resultados de la tabla "libro".
- En caso de que id sea mayor a cero (id>0) deben imprimir solamente el libro correspondiente a ese id.
- Deben usar la sentencia "filter" cuando se desea visualizar un libro en particular.
IMPORTANTE: Es posible que pasen como id un número no definido en la tabla y el sistema de fetchone les devuelva None, lo cual es correcto, pero el sistema no debe explotar porque haya retornado None. En ese caso pueden imprimir en pantalla que no existe ese libro en la base de datos.

## search_author(book_title)
Deben crear una función que retorne el autor que pertenece al título del libro pasado como parámetro a esta función. Deben crear una query usando la sentencia "join" junto con "filter" para buscar el autor correspondiente al libro.\
Al finalizar la función rebe retornar el autor:
```
    return author
```

## Esquema del ejercicio
Deben crear su archivo de python y crear las funciones mencionadas en este documento. Deben crear la sección "if _name_ == "_main_" y ahí crear el flujo de prueba de este programa:
```
if __name__ == "__main__":
  # Crear DB
  create_schema()

  # Completar la DB con el CSV
  fill()

  # Leer filas
  fetch()  # Ver todo el contenido de la DB
  fetch(3)  # Ver la fila 3
  fetch(20)  # Ver la fila 20

  # Buscar autor
  print(search_author('Relato de un naufrago'))

```
