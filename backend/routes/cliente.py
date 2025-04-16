from flask import Blueprint, request, jsonify
from models import db
from models.cliente import Cliente

cliente_bp = Blueprint('cliente_bp', __name__, url_prefix='/clientes')

@cliente_bp.route('/', methods=['GET'])
def get_clientes():
    clientes = Cliente.query.all()
    return jsonify([{
        'id': c.id,
        'nombre': c.nombre,
        'telefono': c.telefono,
        'email': c.email,
        'direccion': c.direccion
    } for c in clientes])

@cliente_bp.route('/', methods=['POST'])
def create_cliente():
    data = request.get_json()
    nuevo_cliente = Cliente(
        nombre=data['nombre'],
        telefono=data['telefono'],
        email=data['email'],
        direccion=data['direccion']
    )
    db.session.add(nuevo_cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente creado'}), 201

@cliente_bp.route('/<int:id>', methods=['GET'])
def get_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    return jsonify({
        'id': cliente.id,
        'nombre': cliente.nombre,
        'telefono': cliente.telefono,
        'email': cliente.email,
        'direccion': cliente.direccion
    })

@cliente_bp.route('/<int:id>', methods=['PUT'])
def update_cliente(id):
    data = request.get_json()
    cliente = Cliente.query.get_or_404(id)
    cliente.nombre = data['nombre']
    cliente.telefono = data['telefono']
    cliente.email = data['email']
    cliente.direccion = data['direccion']
    db.session.commit()
    return jsonify({'mensaje': 'Cliente actualizado'})

@cliente_bp.route('/<int:id>', methods=['DELETE'])
def delete_cliente(id):
    cliente = Cliente.query.get_or_404(id)
    db.session.delete(cliente)
    db.session.commit()
    return jsonify({'mensaje': 'Cliente eliminado'})
