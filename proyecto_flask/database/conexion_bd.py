import mysql.connector

class ConexionBD:
    def __init__(self, usuario, contrasena, host, base_datos):
        self.usuario = usuario
        self.contrasena = contrasena
        self.host = host
        self.base_datos = base_datos
        self.cnx = None

    def conectar(self):
        self.cnx = mysql.connector.connect(user=self.usuario, password=self.contrasena, host=self.host, database=self.base_datos)
        return self.cnx.cursor()

    def cerrar(self):
        if self.cnx is not None:
            self.cnx.close()

