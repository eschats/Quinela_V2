from sqlite3 import Cursor
from flask import Flask ,jsonify, render_template
from config import config
from flask_mysqldb import MySQL



# Inicializar el app 
app = Flask(__name__)

conexion = MySQL(app)


# Listar todos los usuarios dentro de la herramienta
@app.route('/registrarliga/obtenerequipos', methods = ['GET'])
def listar_equipo():
    try:
        cursor = conexion.connection.cursor()
        sql="SELECT * FROM EQUIPO"
        cursor.execute(sql)
        datos=cursor.fetchall()
        equipos =[]
        for fila in datos:
            equipo={'ID_EQUIPO':fila[0],'NOMBRE':fila[1]}
            equipos.append(equipo)
        return jsonify({'usuarios':equipos, 'mensaje': "equipos creados"}) 
    except Exception as ex:
        return jsonify({'mensaje': "registros no encontrados"}) 

def pagina_no_encontrada(error):
    return "<h1> La pagina no existe <h1>",404


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()