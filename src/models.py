from sqlalchemy import Integer, Column, String, ForeignKey, Date, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import datetime as dt
import config

Base = declarative_base()

class Anuncio(Base):
    __tablename__ = 'anuncio'
    id = Column(Integer, primary_key=True)
    precio = Column(Integer)
    cuerpo = Column(Text)
    titulo = Column(Text)
    publicado = Column(Date, nullable=True)
    anuncio_id = Column(String(500), nullable=False)
    url = Column(String(500), nullable=False)
    busqueda_id = Column(Integer, ForeignKey('busqueda_segundamano.id'))

    def __str__(self):
        return '{} ${}'.format(self.titulo, self.precio)


class Imagen(Base):
    __tablename__ = 'imagen'
    
    id = Column(Integer, primary_key=True)
    url = Column(String(500))
    anuncio_id = Column(Integer, ForeignKey('anuncio.id'))

class BusquedaSegundaMano(Base):
    __tablename__ = 'busqueda_segundamano'

    id = Column(Integer, primary_key=True)
    palabras = Column(String(500), nullable=False)
    region = Column(Integer, nullable=True)
    fecha_inicio = Column(Date, nullable=False)
    precio_maximo = Column(Date, nullable=False)

    def __str__(self):
        return 'precio_maximo:${} region:{} palabras:{}'.format(self.precio_maximo, self.region, self.palabras)

engine = create_engine(config.url)
Base.metadata.create_all(engine)
