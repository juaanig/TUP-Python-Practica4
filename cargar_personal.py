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

    def crearCod(self):
        self.codID= 'PQ_'+ str(self.dni)[5:9]
        
    def cargarCodPeluquero(self):
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
        for peluquero in peluqueros:
            print(peluquero[0],peluquero[1],peluquero[2],peluquero[3],peluquero[4],peluquero[5],peluquero[6],peluquero[7])
            print("\n")
        conexion.cerrarConexion()


'''prueba.crearCod()
prueba.cargarCodPeluquero()'''


#############################################################################################################################


class Recepcionista(Personal):

    def crearCod(self):
        self.codID= 'RE_'+ str(self.dni)[5:9]

    def cargarCodRecepcionista(self):
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO RECEPCIONISTA VALUES('{}','{}','{}','{}','{}','{}','{}','{}') ".format(self.codID,self.nombre,self.apellido,self.dni,self.direccion,self.telefono,self.email,self.sueldo))
        conexion.miConexion.commit()
        conexion.cerrarConexion()
        print("###### RECEPCIONISTA CARGADO EXITOSAMENTE ######")   

'''prueba= Recepcionista('Jose','Pereeeeez',43497777,'calle falsa 123',1234567890,'fran@gmail.com',12000)
prueba.crearCod()
prueba.cargarCodRecepcionista()'''




