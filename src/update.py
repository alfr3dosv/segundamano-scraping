from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Anuncio, Imagen, BusquedaSegundaMano
from scrapper import buscar, insertar_anuncio
from session import session

busquedas = session.query(BusquedaSegundaMano).all()

for b in busquedas:
    for id, json in buscar(b.palabras, '1').items():
        existe = session.query(Anuncio).filter(Anuncio.anuncio_id == id).first()
        if existe == None:
            insertar_anuncio(json)

