from flask import Flask, request, render_template
from flask_restful import Resource, Api
from config import api_user, api_password
from models import Anuncio, Imagen, BusquedaSegundaMano
from session import session
import json
import datetime as dt
app = Flask(__name__, template_folder='../client', static_folder='../client')
api = Api(app)

@app.route('/')
def index():
    return render_template('app.html')


def is_valid_user(user, password):
    return user is api_user and password is api_password

class ListaPublicaciones(Resource):     
    def get(self, user: int, password: int):
        result = {}
        busquedas = session.query(BusquedaSegundaMano).all()
        for busqueda in busquedas:
            anuncios = session.query(Anuncio).filter(Anuncio.busqueda_id == busqueda.id).all()
            for anuncio in anuncios:
                imagenes = session.query(Imagen).filter(Imagen.anuncio_id == anuncio.id).all()
        return {'nada': 'nada'}
        
class AgregarBusqueda(Resource):
    def post(self):
        data = request.get_json()
        busqueda = BusquedaSegundaMano()
        # busqueda.fecha_inicio = dt.date.fromtimestamp(data['fecha_inicio'])
        busqueda.palabras = data['palabras']
        busqueda.precio_maximo = int(data['precio'])
        busqueda.region = int(data['region'])
        print(busqueda)
        print(data)
        return {'result': 'ok'}

api.add_resource(ListaPublicaciones, '/lista/<int:user>/<int:password>')
api.add_resource(AgregarBusqueda, '/agregar')
if __name__ == '__main__':
    app.run(debug=True)