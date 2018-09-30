import requests, json, datetime as dt
from models import Anuncio, Imagen
from session import session

def buscar(busqueda: str, pagina: int):
    target = 'https://webapi.segundamano.mx/nga/api/v1/public/klfst'
    resultado_json = requests.get(target, params = {
        'region': '21',
        'q': busqueda.replace(' ', '_'),
        'lim': '29',
        'offset': str(pagina),
        'lang': 'es',
        'sort': 'date'
    }).json()

    anuncios_con_ids = {}
    for resultado in resultado_json['list_ads']:
        ad = resultado['ad']
        id = ad['ad_id']
        anuncios_con_ids[str(id)] = ad

    return anuncios_con_ids

def insertar_anuncio(ad: dict):
    anuncio = obtener_anuncio(ad)
    timestamp = int(ad['list_time']['value'])
    anuncio.publicado = str(dt.date.fromtimestamp(timestamp))
    
    session.add(anuncio)
    session.flush()

    for imagen in obtener_imagenes(ad):
        imagen.anuncio_id = anuncio.id
        session.add(imagen)
    
    session.commit()

def obtener_anuncio(ad: dict):
    anuncio = Anuncio()
    timestamp = int(ad['list_time']['value'])
    anuncio.publicado = str(dt.datetime.fromtimestamp(timestamp))

    if 'prices' in ad:
        anuncio.precio = int(ad['list_price']['price_value'])
    anuncio.cuerpo = ad['body']
    anuncio.titulo = ad['subject']
    anuncio.anuncio_id = ad['ad_id']
    anuncio.url = ad['share_link']

    return anuncio

def obtener_imagenes(ad):   
    imagenes = []
    if 'images' in ad:
        imagen = Imagen()
        for i in ad['images']:
            imagen_link = i['base_url'] + '/medium/' + i['path']
            imagen.url = imagen_link
            imagenes.append(imagen)
    
    return imagenes
