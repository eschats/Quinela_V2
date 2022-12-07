from sqlite3 import Cursor
from urllib import request
from flask import Flask ,jsonify, render_template, request
from config import config
from flask_mysqldb import MySQL
from validar import *
import smtplib
from email.message import EmailMessage


# Inicializar el app 
app = Flask(__name__)

conexion = MySQL(app)

#########################REGISTRAR LIGA ################################

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

######################Invitar#############################

@app.route('/Invitar', methods = ['POST'])
def registra_usuario_Invitado():
    try:

       email_subject = "Invitacion al Torneo" 
       sender_email_address = "your_email@gmail.com" 
       receiver_email_address = "receiver_email@address.com" 
       email_smtp = "smtp.gmail.com" 
       email_password = "your_email_password" 

# Create an email message object 
       message = EmailMessage() 

# Configure email headers 
       message['Subject'] = email_subject 
       message['From'] = sender_email_address 
       message['To'] = receiver_email_address 

# Set email body text 
       message.set_content("Hello from Python!") 

# Set smtp server and port 
       server = smtplib.SMTP(email_smtp, '587') 

# Identify this client to the SMTP server 
       server.ehlo() 

# Secure the SMTP connection 
       server.starttls() 

# Login to email account 
       server.login(sender_email_address, email_password) 

# Send email 
       server.send_message(message) 

# Close connection to server 
       server.quit()

       return jsonify({'mensaje': "usuario invitado"}) 
    except Exception as ex:
        return jsonify({'mensaje': "ERROR 0003"}) 


#def listar_usuario():
 #   return render_template('auth/login.html')


######################Obtener Equipos#############################

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

##########################Administrar Grupos################################
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



########################OBTENER LIGAS ###################################


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


######################REGISTRAR UN USUARIO################################
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

####################REGISTRAR UN EQUIPO#######################################
@app.route('/registrar/equipo', methods = ['POST','GET'])
def registra_equipo():
    try:
        curso = leer_equipo(request.json['nombre'])
        if curso != None:
            return jsonify({'mensaje': "Equipo ya creado"}) 
        else:
            cursor = conexion.connection.cursor()
            sql="""INSERT INTO equipo (NOMBRE) VALUES ('{0}')""".format(request.json['nombre'])
            cursor.execute(sql)
            conexion.connection.commit() # confirmaci
            return jsonify({'mensaje': "equipo registrado"}) 
    except Exception as ex:
        return jsonify({'mensaje': "ERROR 0003 <Equipo Ya creado o Falta de datos Json>"}) 



def leer_equipo(codigo):
    try:
        cursor = conexion.connection.cursor()
        sql = "SELECT NOMBRE FROM equipo WHERE NOMBRE = '{0}'".format(codigo)
        cursor.execute(sql)
        datos = cursor.fetchone()
        if datos != None:
            curso = {'codigo': datos[0]}
            return curso
        else:
            return None
    except Exception as ex:
        raise ex

##################RELACIÓN GRUPO EQUIPO########################
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


###########################DETENER EL SERVIDOR##################################
def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

@app.route('/shutdown', methods=['POST'])
def shutdown():
    shutdown_server()
    return 'Server shutting down...'





if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()