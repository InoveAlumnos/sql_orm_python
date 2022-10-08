__author__ = "Damian Safdie"
__email__ = "damiansafdie@gmail.com"


import csv
import sqlalchemy

# SqlAlchemy
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

# Creo el motor (engine) de la base de datos
engine = sqlalchemy.create_engine("sqlite:///articulos_mercadolibre.db")
base = declarative_base()


class Articulo(base):
    __tablename__ = 'articulo'
    id = Column(String, primary_key=True, autoincrement=False)
    site_id = Column(String)
    title = Column(String)
    price = Column(Integer)
    currency_id = Column(String)
    initial_quantity = Column(Integer)
    available_quantity = Column(Integer)
    sold_quantity = Column(Integer)

    def __repr__(self):
        return f'Articulo\nId: {self.id}\nSite id: {self.site_id}\nTitle: {self.title}\
                 \nPrice: {self.price}\nCurrency id: {self.currency_id},\nInitial Quantity: {self.initial_quantity}\
                 \nAvailable Quantity: {self.initial_quantity}\nSold Quantity: {self.sold_quantity}'


def create_schema():
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)

def fill():
    Session = sessionmaker(bind=engine)
    session = Session()

    #tutor = Tutor(name='Julian')
    #session.add(tutor)        
    
    session.commit()    


if __name__ == "__main__":
  create_schema()

  # Completar la DB con el CSV
  #fill()

  # Leer filas
  #fetch('MLA845041373')
  #fetch('MLA717159516')





'''
## Para jugar
Cuando finalicen el ejercicio pueden realizar un sistema de compras.
Pueden pasarle a su sistema el carrito de un cliente con todos los IDs
de los productos comprados por la persona y el sistema podría devolver
el monto total de compra.

## Anexo
En la carpeta de anexo encontrará este ejercicio resuelto, como también una forma mejorada utilizando "async" para acelerar drástica mente el código (async no fue visto en clase y 
requeire instalar una librería adicional como se explica en el ejercicio).
'''