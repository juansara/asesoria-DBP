from flask import Flask, jsonify, url_for, render_template, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Creamos la apliacion
app = Flask(__name__)

#Configuramos la base de datos
USER_DB = "postgres"
PASSWORD_DB = "admin"
URL_DB = "localhost:5432"
NAME_DB = "asesoria"
FULL_URL_DB = f'postgresql://{USER_DB}:{PASSWORD_DB}@{URL_DB}/{NAME_DB}'

app.config["SQLALCHEMY_DATABASE_URI"] = FULL_URL_DB
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
#Configuramos las migraciones
migrate = Migrate(app,db)

class Persona(db.Model):
    __tablename__ = "persona"
    id = db.Column(db.Integer, nullable = False, primary_key = True)
    nombre = db.Column(db.String(), nullable = False)
    apellido = db.Column(db.String(), nullable = False)
    edad = db.Column(db.Integer, nullable = False)
    ciclo = db.Column(db.Integer, nullable = False)
    carrera = db.Column(db.String(), nullable = False)
    
    def __repr__(self):
        return f'Nombre:{self.nombre} Apellido:{self.apellido} Edad:{self.edad} Ciclo:{self.ciclo} Carrera:{self.carrera} Descripcion:{self.descripcion}'

@app.route('/', methods=['GET'])
def index():
    return 0

@app.route('/agregar', methods=['POST'])
def agregar():
    return 0

@app.route('/actualizar/<int:id>', methods=[''])
def actualizar(id):
    return 0

@app.route('/delete/<int:id>', methods=['DELETE'])
def eliminar(id):
    return 0