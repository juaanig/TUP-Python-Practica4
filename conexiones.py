import sqlite3

class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()

''' 
#Creacion de tabla
miCursor.execute("""CREATE TABLE IF NOT EXISTS DATOS (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    NOMBRE_PERRO VARCHAR(50),
    NOMBRE_DUEÑO VARCHAR(50),
    DOMICILIO VARCHAR(50), 
    TEL INTEGER(11))
    """)
'''