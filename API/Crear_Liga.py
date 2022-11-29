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
@app.route('/registrarliga', methods = ['POST','GET'])

def registra_liga():
    
    try:
        ligas = tipo(request.json['tipo'])
        if ligas == True:
            cursor = conexion.connection.cursor()
            sql="""INSERT INTO liga  (NOMBRE_LIGA,TIPO,COSTO) VALUES ('{0}','{1}','{2}')""".format(request.json['liga'],request.json['tipo'],request.json['costo'])
            cursor.execute(sql)
            conexion.connection.commit() # confirmaci
            return jsonify({'mensaje': "Liga Ingresada"}) 
        else:
             return jsonify({'mensaje': "Tipo de Liga no existente"})
    except Exception as ex:
        return jsonify({'mensaje': "ERROR 0003 <Liga Ya creado o Falta de datos Json>"}) 

def pagina_no_encontrada(error):
    return "<h1> La pagina no existe <h1>",404


   



def pagina_no_encontrada(error):
    return "<h1> La pagina no existe <h1>",404



#def listar_usuario():
 #   return render_template('auth/login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()