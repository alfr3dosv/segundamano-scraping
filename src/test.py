from requests import post
import json
data = {
    'user': 'Alfredo',
    'password': 'pass',
    'palabras': 'algo',
    'fecha_inicio': '45454',
    'precio_maximo': '0',
    'region': '0'
}

print(post('http://localhost:5000/agregar', json=json.dumps(data)))