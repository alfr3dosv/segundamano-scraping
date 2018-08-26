import requests, json, datetime as dt
from models import Anuncio, Imagen
from session import session

def buscar(busqueda, pagina):
    target = 'https://webapi.segundamano.mx/nga/api/v1/public/klfst'
    resultado_json = requests.get(target, params = {
        'region': '21',
        'q': busqueda.replace(' ', '_'),
        'lim': '29',
        'offset': str(pagina),
        'lang': 'es'
    }).json()

    anuncios_con_ids = {}
    for resultado in resultado_json['list_ads']:
        ad = resultado['ad']
        id = ad['ad_id']
        anuncios_con_ids[str(id)] = ad

    return anuncios_con_ids

def insertar_anuncio(ad):
    anuncio = Anuncio()
    if 'prices' in ad:
        anuncio.precio = int(ad['list_price']['price_value'])
    anuncio.cuerpo = ad['body']
    anuncio.titulo = ad['subject']
    anuncio.anuncio_id = ad['ad_id']
    anuncio.url = ad['share_link']
    timestamp = int(ad['list_time']['value'])
    anuncio.publicado = str(dt.datetime.fromtimestamp(timestamp))
    
    session.add(anuncio)
    session.flush()

    for imagen in obtener_imagenes(ad):
        imagen.anuncio_id = anuncio.id
        session.add(imagen)
    
    session.commit()

def obtener_imagenes(ad):   
    imagenes = []
    if 'images' in ad:
        imagen = Imagen()
        for i in ad['images']:
            imagen_link = i['base_url'] + '/medium/' + i['path']
            imagen.url = imagen_link
            imagenes.append(imagen)
    
    return imagenes
