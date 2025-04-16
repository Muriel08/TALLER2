from models import db

class Vehiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50), nullable=False)
    patente = db.Column(db.String(20), unique=True, nullable=False)
    anio = db.Column(db.Integer, nullable=False)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), nullable=False)
    reparaciones = db.relationship('Reparacion', backref='vehiculo', cascade="all, delete-orphan")
