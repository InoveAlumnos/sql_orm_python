__author__ = "Damian Safdie"
__email__ = "damiansafdie@gmail.com"

import csv
import requests
import sqlalchemy


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
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


def agrego_db(dato):
    Session = sessionmaker(bind=engine)
    session = Session()   
    articulo = Articulo(id=dato['id'], site_id=dato['site_id'], title=dato['title'], price=dato['price'],
                    currency_id=dato['currency_id'], initial_quantity=dato['initial_quantity'],
                    available_quantity=dato['available_quantity'], sold_quantity=dato['sold_quantity'])
    session.add(articulo)
    session.commit()
    

def fill():
    with open('meli_technical_challenge_data.csv', 'r') as arch:
        data = list(csv.DictReader(arch))
        for x in data:
            item = x['site'] + x['id']
            print(" Generando: ", item)
            url = 'https://api.mercadolibre.com/items?ids={}'.format(item)
            try:
                un_dato = requests.get(url).json()        
                dato = un_dato[0]['body']
                agrego_db(dato)                
            except:
                pass
                   
def fetch(dato):
    print ("comsulta para el codigo:", dato)
    Session = sessionmaker(bind=engine)
    session = Session()
    result = session.query(Articulo).filter(Articulo.id == dato)
    if result.count() > 0:        
        for x in result:
            print(x)
    else:
        print ("Inexixtente")


if __name__ == "__main__":
  create_schema()
  fill()
  fetch('MLA845041373')
  fetch('MLA717159516')
  fetch('MLA843335445')
  fetch('MLA843675412')

