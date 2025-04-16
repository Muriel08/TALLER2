from flask import Blueprint, request, jsonify
from models import db
from models.reparacion import Reparacion
from datetime import datetime

reparacion_bp = Blueprint('reparacion_bp', __name__, url_prefix='/reparaciones')

@reparacion_bp.route('/', methods=['GET'])
def get_reparaciones():
    reparaciones = Reparacion.query.all()
    return jsonify([{
        'id': r.id,
        'fecha': r.fecha.strftime('%Y-%m-%d'),
        'descripcion': r.descripcion,
        'trabajos_realizados': r.trabajos_realizados,
        'costo': str(r.costo),
        'vehiculo_id': r.vehiculo_id
    } for r in reparaciones])

@reparacion_bp.route('/', methods=['POST'])
def create_reparacion():
    data = request.get_json()
    nueva_reparacion = Reparacion(
        fecha=datetime.strptime(data['fecha'], '%Y-%m-%d'),
        descripcion=data['descripcion'],
        trabajos_realizados=data['trabajos_realizados'],
        costo=data['costo'],
        vehiculo_id=data['vehiculo_id']
    )
    db.session.add(nueva_reparacion)
    db.session.commit()
    return jsonify({'mensaje': 'Reparación creada'}), 201

@reparacion_bp.route('/<int:id>', methods=['GET'])
def get_reparacion(id):
    r = Reparacion.query.get_or_404(id)
    return jsonify({
        'id': r.id,
        'fecha': r.fecha.strftime('%Y-%m-%d'),
        'descripcion': r.descripcion,
        'trabajos_realizados': r.trabajos_realizados,
        'costo': str(r.costo),
        'vehiculo_id': r.vehiculo_id
    })

@reparacion_bp.route('/<int:id>', methods=['PUT'])
def update_reparacion(id):
    data = request.get_json()
    reparacion = Reparacion.query.get_or_404(id)
    reparacion.fecha = datetime.strptime(data['fecha'], '%Y-%m-%d')
    reparacion.descripcion = data['descripcion']
    reparacion.trabajos_realizados = data['trabajos_realizados']
    reparacion.costo = data['costo']
    reparacion.vehiculo_id = data['vehiculo_id']
    db.session.commit()
    return jsonify({'mensaje': 'Reparación actualizada'})

@reparacion_bp.route('/<int:id>', methods=['DELETE'])
def delete_reparacion(id):
    reparacion = Reparacion.query.get_or_404(id)
    db.session.delete(reparacion)
    db.session.commit()
    return jsonify({'mensaje': 'Reparación eliminada'})
