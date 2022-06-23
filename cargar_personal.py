from conexiones import Conexiones

class Personal():

    def  __init__(self,nombre,apellido,dni,direccion,telefono,email,sueldo,exp=0):
        self.nombre=nombre
        self.apellido=apellido
        self.dni=dni
        self.direccion = direccion
        self.telefono=telefono
        self.email=email
        self.sueldo=sueldo
        self.exp=exp


class Peluquero(Personal):
 
    def cargarCodPeluquero(self):
        self.codID= 'PQ_'+ str(self.dni)[-3:]
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO PELUQUEROS VALUES('{}','{}','{}','{}','{}','{}','{}','{}','{}') ".format(self.codID,self.nombre,self.apellido,self.dni,self.direccion,self.telefono,self.email,self.sueldo,self.exp))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
        print("###### PELUQUERO CARGADO EXITOSAMENTE ######")

    @classmethod
    def listado_peluqueros(self,monto):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("SELECT * FROM PELUQUEROS WHERE SUELDO > {}".format(monto))
        peluqueros = conexion.miCursor.fetchall()
        conexion.cerrarConexion()
        return peluqueros

#############################################################################################################################
class Recepcionista(Personal):

    def cargarCodRecepcionista(self):
        self.codID= 'RE_'+ str(self.dni)[-3:]
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO RECEPCIONISTA VALUES('{}','{}','{}','{}','{}','{}','{}','{}') ".format(self.codID,self.nombre,self.apellido,self.dni,self.direccion,self.telefono,self.email,self.sueldo))
        conexion.miConexion.commit()
        conexion.cerrarConexion()  

    @classmethod
    def listado_recepcionistas(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("SELECT * FROM RECEPCIONISTA")
        recepcionista = conexion.miCursor.fetchall()
        conexion.cerrarConexion()
        return recepcionista