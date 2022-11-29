from sqlite3 import Cursor
from flask import Flask ,jsonify, render_template
from config import config
from flask_mysqldb import MySQL



# Inicializar el app 
app = Flask(__name__)

conexion = MySQL(app)


# Listar todos los usuarios dentro de la herramienta
@app.route('/registrarliga/ligas', methods = ['GET'])
def listar_ligas():
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT NOMBRE_LIGA, TIPO, COSTO FROM LIGA"
        cursor.execute(sql)
        datos=cursor.fetchall()
        ligas =[]
        for fila in datos:
            liga={'NOMBRE_LIGA':fila[0],'TIPO':fila[1],'COSTP':fila[2]}
            ligas.append(liga)
        return jsonify({'usuarios':ligas, 'mensaje': "ligas creados"}) 
    except Exception as ex:
        return jsonify({'mensaje': "usuarios no encontrados"}) 

def pagina_no_encontrada(error):
    return "<h1> La pagina no existe <h1>",404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()