from flask import Blueprint, request, jsonify
from models import db
from models.vehiculo import Vehiculo

vehiculo_bp = Blueprint('vehiculo_bp', __name__, url_prefix='/vehiculos')

@vehiculo_bp.route('/', methods=['GET'])
def get_vehiculos():
    vehiculos = Vehiculo.query.all()
    return jsonify([{
        'id': v.id,
        'marca': v.marca,
        'modelo': v.modelo,
        'patente': v.patente,
        'anio': v.anio,
        'cliente_id': v.cliente_id
    } for v in vehiculos])

@vehiculo_bp.route('/', methods=['POST'])
def create_vehiculo():
    data = request.get_json()
    nuevo_vehiculo = Vehiculo(
        marca=data['marca'],
        modelo=data['modelo'],
        patente=data['patente'],
        anio=data['anio'],
        cliente_id=data['cliente_id']
    )
    db.session.add(nuevo_vehiculo)
    db.session.commit()
    return jsonify({'mensaje': 'Vehículo creado'}), 201

@vehiculo_bp.route('/<int:id>', methods=['GET'])
def get_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    return jsonify({
        'id': vehiculo.id,
        'marca': vehiculo.marca,
        'modelo': vehiculo.modelo,
        'patente': vehiculo.patente,
        'anio': vehiculo.anio,
        'cliente_id': vehiculo.cliente_id
    })

@vehiculo_bp.route('/<int:id>', methods=['PUT'])
def update_vehiculo(id):
    data = request.get_json()
    vehiculo = Vehiculo.query.get_or_404(id)
    vehiculo.marca = data['marca']
    vehiculo.modelo = data['modelo']
    vehiculo.patente = data['patente']
    vehiculo.anio = data['anio']
    vehiculo.cliente_id = data['cliente_id']
    db.session.commit()
    return jsonify({'mensaje': 'Vehículo actualizado'})

@vehiculo_bp.route('/<int:id>', methods=['DELETE'])
def delete_vehiculo(id):
    vehiculo = Vehiculo.query.get_or_404(id)
    db.session.delete(vehiculo)
    db.session.commit()
    return jsonify({'mensaje': 'Vehículo eliminado'})
