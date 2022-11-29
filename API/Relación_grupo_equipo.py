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
@app.route('/registrar/relaciónequipo', methods = ['POST','GET'])
def relación_equipo():
    try:
        curso = leer_equipo1(request.json['equipo'])
        curso1 = leer_grupo1(request.json['grupo'])
        if curso == None and curso1 == None:
            return jsonify({'mensaje': "EQUIPO O GRUPO NO EXISTE"}) 
        else:
            cursor = conexion.connection.cursor()
            sql="""INSERT INTO relacion_grupo (EQUIPO_ID_EQUIPO,GRUPO_ID_GRUPO) VALUES ('{0}','{1}')""".format(request.json['equipo'],request.json['grupo'])
            cursor.execute(sql)
            conexion.connection.commit() # confirmaci
            return jsonify({'mensaje': "relacion de equipo creada ya"}) 

    except Exception as ex:
        return jsonify({'mensaje': "ERROR 0005 <Equipo Ya creado o Falta de datos Json>"}) 



def leer_equipo1(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM equipo WHERE ID_EQUIPO = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex


def leer_grupo1(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT * FROM grupo_estado WHERE ID_GRUPO = '{0}'".format(codigo)
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