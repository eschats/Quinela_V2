from sqlite3 import Cursor
from urllib import request
from flask import Flask ,jsonify, render_template, request
from config import config
from flask_mysqldb import MySQL
from validar import *


# Inicializar el app 
app = Flask(__name__)

conexion = MySQL(app)


# Listar todos los usuarios dentro de la herramienta
@app.route('/registrar', methods = ['POST'])
def registra_usuario():
    try:
       correo = '{0}'.format(request.json['correo'])
       email = is_valid_email(correo)
       if email == True:
            cursor = conexion.connection.cursor()
            sql="""INSERT INTO usuario (CORREO,NOMBRE, APELLIDO, CONTRASEÑA, ROL_ID_ROL) VALUES ('{0}','{1}','{2}','{3}','{4}')""".format(request.json['correo'],request.json['nombre'],request.json['apellido'],request.json['contraseña'],request.json['rol'])
            cursor.execute(sql)
            conexion.connection.commit() # confirmaci
            return jsonify({'mensaje': "usuario registrado"}) 
       else:
        return jsonify({'mensaje': "formato de correo incorrecto"}) 

    except Exception as ex:
        return jsonify({'mensaje': "ERROR 0003 <Usuario Ya creado o Falta de datos Json>"}) 

def pagina_no_encontrada(error):
    return "<h1> La pagina no existe <h1>",404



#def listar_usuario():
 #   return render_template('auth/login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()