from app import app
from models import db
from models.cliente import Cliente

with app.app_context():
    db.create_all()
    cliente = Cliente(nombre='Juan Pérez', telefono='123456789', email='juan@example.com', direccion='Calle Falsa 123')
    db.session.add(cliente)
    db.session.commit()
