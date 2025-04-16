from flask import Blueprint
from routes.cliente import cliente_bp
from routes.vehiculo import vehiculo_bp
from routes.reparacion import reparacion_bp

def register_blueprints(app):
    app.register_blueprint(cliente_bp)
    app.register_blueprint(vehiculo_bp)
    app.register_blueprint(reparacion_bp)
