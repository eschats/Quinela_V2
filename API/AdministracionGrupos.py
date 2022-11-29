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
@app.route('/registrar/grupo', methods = ['POST','GET'])
def registra_grupo():
    try:
        curso = leer_grupo(request.json['nombre'])
        if curso != None:
            return jsonify({'mensaje': "Grupo ya creado"}) 
        else:
            cursor = conexion.connection.cursor()
            sql="""INSERT INTO grupo_estado (NOMBRE) VALUES ('{0}')""".format(request.json['nombre'])
            cursor.execute(sql)
            conexion.connection.commit() # confirmaci
            return jsonify({'mensaje': "Grupo registrado"}) 
            
            

    except Exception as ex:
        return jsonify({'mensaje': "ERROR 0003 <Grupo Ya creado o Falta de datos Json>"}) 



def leer_grupo(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT NOMBRE FROM grupo_estado WHERE NOMBRE = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex


def pagina_no_encontrada(error):
    return "<h1> La pagina no existe <h1>",404



#def listar_usuario():
 #   return render_template('auth/login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()