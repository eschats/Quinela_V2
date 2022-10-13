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


# Listar todos los usuarios dentro de la herramienta
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

def pagina_no_encontrada(error):
    return "<h1> La pagina no existe <h1>",404



#def listar_usuario():
 #   return render_template('auth/login.html')


if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404, pagina_no_encontrada)
    app.run()