#!/usr/bin/env python
'''
SQL ORM [Python]
Ejemplos de clase
---------------------------
Autor: Inove Coding School
Version: 2.0

Descripcion:
Programa creado para mostrar ejemplos prácticos de los visto durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "2.0"

# https://extendsclass.com/sqlite-browser.html

import csv
import sqlalchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Crear el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///personas_nacionalidad.db")
base = declarative_base()


class Nacionalidad(base):
    __tablename__ = "nacionalidad"
    id = Column(Integer, primary_key=True)
    country = Column(String)
    
    def __repr__(self):
        return f"Nacionalidad: {self.country}"


class Persona(base):
    __tablename__ = "persona"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    nacionalidad_id = Column(Integer, ForeignKey("nacionalidad.id"))

    nationality = relationship("Nacionalidad")

    def __repr__(self):
        return f"Persona:{self.name} con nacionalidad {self.nationality.country}"


def create_schema():

    # Borrar todos las tablas existentes en la base de datos
    # Esta linea puede comentarse sino se eliminar los datos
    base.metadata.drop_all(engine)

    # Crear las tablas
    base.metadata.create_all(engine)


def insert_nacionalidad(country):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Crear una nueva nacionalidad
    nationality = Nacionalidad(country=country)

    # Agregar la nacionalidad a la DB
    session.add(nationality)
    session.commit()
    print(nationality)


def insert_persona(name, age, country):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar la nacionalidada nueva nacionalidad
    query = session.query(Nacionalidad).filter(Nacionalidad.country == country)
    nationality = query.first()

    if nationality is None:
        # Podrá ver en este ejemplo que sucederá este error con la persona
        # de nacionalidad Inglaterra ya que no está definida en el archivo
        # de nacinoalidades
        print(f"Error la crear la persona {name}, no existe la nacionalidad {country}")
        return

    # Crear la persona
    person = Persona(name=name, age=age, nationality=nationality)

    # Agregar la persona a la DB
    session.add(person)
    session.commit()
    print(person)


def fill():
    # Insertar el archivo CSV de nacionalidades
    # Insertar fila a fila
    with open('nacionalidad.csv') as fi:
        data = list(csv.DictReader(fi))

    for row in data:
        insert_nacionalidad(row['nationality'])

    # Insertar el archivo CSV de personas
    # Insertar todas las filas juntas
    with open('persona.csv') as fi:
        data = list(csv.DictReader(fi))

    for row in data:
        insert_persona(row['name'], int(row['age']), row['nationality_id'])


def show(limit=0):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todas las personas
    query = session.query(Persona).order_by(Persona.age.desc())

    # Si está definido el limite aplicarlo
    if limit > 0:
        query = query.limit(limit)

    # Leer una persona a la vez e imprimir en pantalla
    for persona in query:
        print(persona)


def get_all():
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar todas las personas
    query = session.query(Persona)
    personas = query.all()

    return personas


def update_persona_nationality(name, country):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Buscar la nacionalidada que se desea actualizar
    query = session.query(Nacionalidad).filter(Nacionalidad.country == country)
    nationality = query.first()

    # Buscar la persona que se desea actualizar
    query = session.query(Persona).filter(Persona.name == name)
    person = query.first()

    # Actualizar la nacionalidad de la persona con nombre "name"
    person.nationality = nationality

    # Aunque la persona ya existe, como el id coincide
    # se actualiza sin generar una nueva entrada en la DB
    session.add(person)
    session.commit()

    print('Persona actualizada', name)


def delete_persona(name):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Borrar la persona con nombre "name"
    rowcount = session.query(Persona).filter(Persona.name == name).delete().rowcount
    session.commit()

    print('Filas actualizadas:', rowcount)


def count_persona(nationality):
    # Crear la session
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(Persona).join(Persona.nationality).filter(Nacionalidad.country == nationality).count()
    return result


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    create_schema()

    # Insertar nacionalidades y personas
    fill()
    show()

    personas = get_all()
    print("Personas en la base de datos:")
    print(personas)

    result = count_persona('Argentina')
    print('Personas encontradas de Argentina:', result)

    update_persona_nationality('Max', 'Holanda')
    show(2)

    insert_persona('Max', 40, 'Estados Unidos')
    insert_persona('SQL', 13, 'Inglaterra')
    insert_persona('SQLite', 20, 'Estados Unidos')
    
    show()
