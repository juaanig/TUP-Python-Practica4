import sqlite3

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()

    def crearTablas(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        self.miCursor.execute("""CREATE TABLE PELUQUEROS(
                    CODID VARCHAR(7) PRIMARY KEY,
                    NOMBRE VARCHAR(50),
                    APELLIDO VARCHAR(50),
                    DNI INTEGER(8),
                    DIRECCION VARCHAR(50), 
                    TEL INTEGER(11),
                    EMAIL VARCHAR(50),
                    SUELDO INTEGER(10),
                    EXPERIENCIA INTEGER(2))""")

        self.miCursor.execute("""CREATE TABLE RECEPCIONISTA(
                    CODID VARCHAR(7) PRIMARY KEY,
                    NOMBRE VARCHAR(50),
                    APELLIDO VARCHAR(50),
                    DNI INTEGER(8),
                    DIRECCION VARCHAR(50), 
                    TEL INTEGER(11),
                    EMAIL VARCHAR(50),
                    SUELDO INTEGER(10))""")

        self.miCursor.execute("""CREATE TABLE PERROS (
                    NOMBRE_PERRO VARCHAR(30) COLLATE NOCASE UNIQUE,
                    NOMBRE_DUEÑO VARCHAR(30),
                    DIRECCION VARCHAR(30),
                    TELEFONO INTEGER(11),
                    BAÑO NUMERIC,
                    BAYCO NUMERIC,
                    COMPORTAMIENTO TEXT(10))""")

        self.miConexion.commit()
        self.cerrarConexion()