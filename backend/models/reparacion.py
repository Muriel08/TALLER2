from models import db

class Reparacion(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    trabajos_realizados = db.Column(db.Text, nullable=False)
    costo = db.Column(db.Numeric(10, 2), nullable=False)
    vehiculo_id = db.Column(db.Integer, db.ForeignKey('vehiculo.id'), nullable=False)
