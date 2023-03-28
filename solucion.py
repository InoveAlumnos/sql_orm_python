# IMPORTANTE: NO borrar los comentarios

import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


# IMPORTANTE
# Debe utilizar la base de datos "libreria.db"
# que se encuentra disponible en el repositorio de clase

# Estructura de la base de datos:
# * Tabla autores *
# - id [integer] --> id del autor --> número (autoincremental)
# - name [text] --> nombre del autor

# * Tabla libros *
# - id [integer] --> id del libro --> número (autoincremental)
# - titulo [text] --> Título del libro
# - cantidad_paginas [integer] --> Cantidad de páginas del libro
# - autor [relationship] --> Nombre del autor del libro

# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///libreria.db")
base = declarative_base()


class Autores(base):
    __tablename__ = "autores"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return f"Autor: {self.name}"


class Libros(base):
    __tablename__ = "libros"
    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    cantidad_paginas = Column(Integer)
    autor_id = Column(Integer, ForeignKey("autores.id"))

    autor = relationship("Autores")

    def __repr__(self):
        return f"Libro {self.titulo} escrito por {self.autor.name}"



def get_all():
    print('Comprobemos su contenido, ¿qué hay en la tabla?')
    # Alumno:
    # Obtener todos los libros de la base de datos
   
    # Estaba función debe retornar al programa principal
    # los libros de la base de datos obtenidos
    # en la query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todas las personas
    query = session.query(Libros)
    libros = query.all()

    return libros


def search_by_autor(autor):
    print('¡Operación búsqueda!')
    # Alumno:
    # Utilizar la sentencia filter para retornar
    # aquellos libros que hayan sido escritos por
    # el autor pasado por parámetro

    # Retornar la lista de libros que retorna la query
    # Puede utilizar all() para obtener
    # todos los libros encontrados por la query
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todas las personas
    query = session.query(Libros).join(Autor).filter(Autor.name==autor)
    libros = query.all()

    return libros


def cantidad_paginas(autor):
    print(f"¿Cuántas páginas escribio {autor}?")
    # Alumno:
    # Esta función debe retornar la suma de todas
    # las páginas que escribió el autor pasado
    # por parámetro en todos sus libros
    # que haya escrito el autor

    # Recomendamos obtener todos lis libros
    # que haya escrito el autor utilizando filter(..)
    # y luego con un bucle sumar la cantidad de páginas

    # Esta función debe retoronar
    # la cantidad de páginas que el autor
    # a escrito en total
    # ¡DEBE RETORNAR UN ENTERO! (int)

    Session = sessionmaker(bind=engine)
    session = Session()

    total_cantidad_paginas = 0

    # Buscar todas las personas
    query = session.query(Libros).join(Autor).filter(Autor.name==autor)
    libros = query.all()
    for libro in libros:
        total_cantidad_paginas += libro.cantidad_paginas

    return total_cantidad_paginas


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    libros = get_all()
