from flask import Flask, jsonify, request
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

app = Flask(__name__)
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()

@app.route('/')
def inicio():
    return("API Lab Redes")

@app.route('/temperatura', methods=['POST'])
def guardar_temperatura():
    temperatura = request.json['temperatura']
    db.collection('dashboard').document('data').update({'temperatura': temperatura})
    return jsonify({'mensaje': 'Temperatura guardada correctamente.'})

@app.route('/presion_atmosferica', methods=['POST'])
def guardar_presion_atmosferica():
    presion_atmosferica = request.json['presion_atmosferica']
    db.collection('dashboard').document('data').update({'presion': presion_atmosferica})
    return jsonify({'mensaje': 'Presión atmosférica guardada correctamente.'})

@app.route('/humedad_relativa', methods=['POST'])
def guardar_humedad_relativa():
    humedad_relativa = request.json['humedad_relativa']
    db.collection('dashboard').document('data').update({'h_relativa': humedad_relativa})
    return jsonify({'mensaje': 'Humedad relativa guardada correctamente.'})

@app.route('/humedad_suelo', methods=['POST'])
def guardar_humedad_suelo():
    humedad_suelo = request.json['humedad_suelo']
    db.collection('dashboard').document('data').update({'h_suelo': humedad_suelo})
    return jsonify({'mensaje': 'Humedad del suelo guardada correctamente.'})


if __name__ == '__main__':
    app.run()
