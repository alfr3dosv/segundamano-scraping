import requests, json
from anuncio import Anuncio

target = 'https://webapi.segundamano.mx/nga/api/v1/public/klfst'

segundamano_request = requests.get(target, params = {
    'region': '21',
    'q': 'gato_negro',
    'lim': '29',
    'offset': '1',
    'lang': 'es'
})

resultado = segundamano_request.json()
print(segundamano_request.url)

def obtener_anuncios(resultado_json):
    resultado = segundamano_request.json()
    print(len(resultado['list_ads']))
    anuncios = []

    for ad in resultado['list_ads']:
        anuncio = Anuncio()
        if 'prices' in ad['ad']:
            anuncio.precio = int(ad['ad']['list_price']['price_value'])
        anuncio.cuerpo = ad['ad']['body']
        anuncio.titulo = ad['ad']['subject']
        anuncio.publicado = ad['ad']['list_time']['value']
        
        for imagen in ad['ad']['images']:
            imagen_link = imagen['base_url'] + '/medium/' + imagen['path']
            anuncio.imagenes.append(imagen_link)

        anuncios.append(anuncio)
    
    return anuncios



for anuncio in obtener_anuncios(resultado):
    print(anuncio)