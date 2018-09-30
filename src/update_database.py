from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Anuncio, Imagen, BusquedaSegundaMano
from scrapper import buscar, insertar_anuncio, obtener_anuncio, obtener_imagenes
from session import session
import datetime as dt
busquedas = session.query(BusquedaSegundaMano).all()

# for b in busquedas:
#     for id, json in buscar(b.palabras, '1').items():
#         existe = session.query(Anuncio).filter(Anuncio.anuncio_id == id).first()
#         if existe == None:
#             insertar_anuncio(json)

# pagina = 1
# publicado = dt.date.today()
# while publicado:
#     resultado:dict = buscar('gato', pagina)
#     if len(resultado) or :
#         break
#     for id, json in resultado.items():
#         anuncio = obtener_anuncio(json)
#         print(obtener_anuncio(json).publicado)
#         if (publicado --)
#     pagina += 1

def actualizar(busqueda: BusquedaSegundaMano):
    valido = True
    while valido:
        pagina = 1
        resultado:dict = buscar('gato', pagina)
        for id, json in resultado.items():
            anuncio = obtener_anuncio(json)
            if anuncio.publicado < busqueda.fecha_inicio:
                valido = False
            if anuncio.precio < busqueda.precio_maximo:
                break
            insertar_anuncio(json)
