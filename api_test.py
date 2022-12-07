import pytest
from main import app as flask_app
import json

#cambio#
############################################INICIALIZAR PRUEBAS ##################################

@pytest.fixture
def app():
    yield flask_app


@pytest.fixture
def client(app):
    return app.test_client()


######################################PRUEBA OBTENER EQUIPOS ####################################
def test_obtenerequipos(app):
    response = app.test_client().get('/registrarliga/obtenerequipos')
    assert response.status_code == 200
  



###################################PRUEBA OBTENER LIGAS #######################################
def test_obtenerligas(app):
    response = app.test_client().get('/registrarliga/ligas')
    assert response.status_code == 200
  
  

###################################PRUEBA OBTENER REGISTRAR LIGAS#######################################
def test_registrarliga(app):
    response = app.test_client().post('/registrarliga')
    assert response.status_code == 200
    response = app.test_client().get('/registrarliga')
    assert response.status_code == 200
  
  

###################################PRUEBA OBTENER ENVIAR INVITACIÓN#######################################
def test_invitar(app):
    response = app.test_client().post('/Invitar')
    assert response.status_code == 200
  
  

  ###################################PRUEBA OBTENER REGISTRAR GRUPOS#######################################
def test_grupos(app):
    response = app.test_client().post('/registrar/grupo')
    assert response.status_code == 200
    response = app.test_client().get('/registrar/grupo')
    assert response.status_code == 200



  ###################################PRUEBA OBTENER REGISTRAR USUARIO#######################################
def test_usuario(app):
    response = app.test_client().post('/registrar')
    assert response.status_code == 200

  
  ###################################PRUEBA OBTENER REGISTRAR EQUIPO#######################################
def test_equipo(app):
    response = app.test_client().post('/registrar/equipo')
    assert response.status_code == 200
    response = app.test_client().get('/registrar/equipo')
    assert response.status_code == 200


  ###################################PRUEBA OBTENER RElACIÓN Y EQUIPO##########################################
def test_relacion_equipo(app):
    response = app.test_client().post('/registrar/relaciónequipo')
    assert response.status_code == 200
    response = app.test_client().get('/registrar/relaciónequipo')
    assert response.status_code == 200


  ###################################PRUEBA DETENER SERVIDOR###########################################3
def test_apagar(app):
    response = app.test_client().post('/shutdown')
    assert response.status_code == 500

