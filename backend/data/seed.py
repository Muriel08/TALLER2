from app import app, db
from models.cliente import Cliente


clientes = [
    Cliente(nombre='Juan Pérez', telefono='123456789', email='juan@example.com', direccion='Calle Falsa 123'),
    Cliente(nombre="Ana Gómez", telefono="987654321", email="ana@example.com", direccion="Av. Rivadavia 456"),
    Cliente(nombre="Carlos Díaz", telefono="1122334455", email="carlos@example.com", direccion="Boulevard 789")
]

with app.app_context():
    for cliente in clientes:
        db.session.add(cliente)
    db.session.commit()
print("✅ Base de datos llena con datos de prueba.")