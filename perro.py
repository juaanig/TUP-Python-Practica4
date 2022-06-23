from conexiones import Conexiones

class Perro:

    #CONSTRUCTOR PARA INSTANCIAS UN OBJETO PERRO CON LOS VALORES RECIBIDOS EN EL CONSTRUCTOR
    def __init__(self, name_dog, name_human,dog_addres,dog_phone,bath,bathhaircut):
        self.nombre_perro = name_dog
        self.nombre_dueño = name_human
        self.direccion = dog_addres
        self.telefono = dog_phone
        self.baño = bath
        self.bayco = bathhaircut
    

    def cargar_perro(self):
        # SI BIEN EN ESTE METODO CARGAMOS AL PERRO ,DEBEMOS INSTANCIAR UN OBJECTO DE LA CLASE 'Conexiones()'
        #  Y CONSUMIR SUS METODOS 'C.R.U.D'
        if self.baño == 1: self.bayco = 0 
        else: self.baño = 1
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO PERROS VALUES('{}','{}','{}','{}','{}','{}','NULL')".format(self.nombre_perro, self.nombre_dueño, self.direccion,self.telefono,self.baño,self.bayco))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
    
    @classmethod
    def modificar_perro(self,arg1,arg2,arg3):
        # MODIFICAREMOS LOS DATOS DE UN PERRO 
        # PRIMERO DEBEMOS ABRIR LA CONEXION CON LA BBDD Y LUEGO APLICAR EL METODO UPDATE 
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("UPDATE PERROS SET DIRECCION='{}',TELEFONO='{}' WHERE NOMBRE_PERRO='{}'".format(arg1,arg2,arg3))
        conexion.miConexion.commit()
        conexion.cerrarConexion()

    @classmethod
    def borrar_perro(self,arg1):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("DELETE FROM PERROS WHERE NOMBRE_PERRO='{}'".format(arg1))
        conexion.miConexion.commit()
        conexion.cerrarConexion()

    @classmethod
    def seleccionar_perro(self,arg1):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("SELECT * FROM PERROS WHERE NOMBRE_PERRO='{}'".format(arg1))
        print(conexion.miCursor.fetchone())
        conexion.miConexion.commit()
        conexion.cerrarConexion()
    
    @classmethod
    def incrementar_motivo(self,arg1,arg2,arg3):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("UPDATE PERROS SET BAÑO=BAÑO+'{}',BAYCO=BAYCO+'{}' WHERE NOMBRE_PERRO='{}'".format(arg1,arg2,arg3))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
    
    @classmethod
    def listado_perros(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("SELECT * FROM PERROS")
        records = conexion.miCursor.fetchall()
        conexion.miConexion.commit()
        conexion.cerrarConexion()
        return records
    
    @classmethod
    def agregar_comportamiento(self,arg1,arg2):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("UPDATE PERROS SET COMPORTAMIENTO='{}' WHERE NOMBRE_PERRO='{}'".format(arg1,arg2))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
    
    @classmethod
    def lista_nombres_perros(self,arg1):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("SELECT NOMBRE_PERRO FROM PERROS WHERE NOMBRE_PERRO='{}'".format(arg1))
        records = conexion.miCursor.fetchone()
        conexion.miConexion.commit()
        conexion.cerrarConexion()
        return True if arg1 in records else False