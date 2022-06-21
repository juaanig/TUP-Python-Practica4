import sqlite3

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()

'''
miConexion=sqlite3.connect("Peluqueria")
miCursor=miConexion.cursor()
miCursor.execute("""CREATE TABLE PELUQUEROS(
                    CODID VARCHAR(7) PRIMARY KEY,
                    NOMBRE VARCHAR(50),
                    APELLIDO VARCHAR(50),
                    DNI INTEGER(8),
                    DIRECCION VARCHAR(50), 
                    TEL INTEGER(11),
                    EMAIL VARCHAR(50),
                    SUELDO INTEGER(10),
                    EXPERIENCIA INTEGER(2))""")


miCursor.execute("""CREATE TABLE RECEPCIONISTA(
                    CODID VARCHAR(7) PRIMARY KEY,
                    NOMBRE VARCHAR(50),
                    APELLIDO VARCHAR(50),
                    DNI INTEGER(8),
                    DIRECCION VARCHAR(50), 
                    TEL INTEGER(11),
                    EMAIL VARCHAR(50),
                    SUELDO INTEGER(10))""")


#Creacion de tabla
miCursor.execute("""CREATE TABLE IF NOT EXISTS DATOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_PERRO VARCHAR(50),
    NOMBRE_DUEÑO VARCHAR(50),
    DOMICILIO VARCHAR(50), 
    TEL INTEGER(11))
    """)
'''