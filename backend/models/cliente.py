from models import db

class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    telefono = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    direccion = db.Column(db.String(150), nullable=False)
    vehiculos = db.relationship('Vehiculo', backref='cliente', cascade="all, delete-orphan")
