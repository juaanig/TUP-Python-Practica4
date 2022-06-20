import sqlite3
"""
Desarrollar un sistema que integre una base de datos con SQLite para una peluquería canina. 
Mediante un menú de opciones llevar a cabo las siguientes posibilidades. 

1- Cargar Perros. 
De cada perro almacenar nombre, nombre del dueño, domicilio, teléfono. Cada perro puede ir a la peluquería por baño, 
o por baño y corte. Por esto mismo almacenar estas dos variables enteras y a medida que el perro vaya por estos motivos 
aumentarlas en 1. El nombre del perro declararlo como Único e irrepetible. Llevar también a cabo un id como primary
key autoincremental. 

2- Modificar datos de un perro. 
Dado el nombre de un perro dar la posibilidad de modificar domicilio o teléfono. 

3- Borrar un perro. 
Dado un nombre de un perro eliminarlo de la base de datos. 
4- Cargar visita. 
Leer el motivo por el que vino el perro (Baño o baño y corte) y aumentar en uno la/s variable/s indicadas. 

5- Listado de Perros. 
Mostrar ordenadamente todos los perros cargados.

0- Salir del menú. 

Punto adicional: usar la estructura de manejo de errores de python para que los datos ingresados sean correctos.
"""

class ProgramaPrincipal:
    
    def menu(self):

        flag = True
        while flag:

            print('\
            \tMENÚ\n\
            1- Cargar Perros.\n\
            2- Modificar datos de un perro.\n\
            3- Borrar un perro.\n\
            4- Cargar visita.\n\
            5- Listado de Perros.\n\
            0- Salir del menú.'
            )
            
            nro = int(input("\nPor favor ingrese un número: "))
            # ==================== OPCION 1 ====================
            if nro == 1:
                baño = 0
                byc = 0
                namePet = input('nombre del firulais: ').upper()
                nameHuman = input('nombre del humano: ').upper()
                address = input('direción: ').upper()
                phone = input('Teléfono: ')
                #______________________________________________________
                selector = input('Motivo de la visita:\n 1-Baño\n 0-Baño y Corte')
                if selector == 1: baño = 1
                elif selector == 0: byc = 1  
                #______________________________________________________
                
                nuevo_perro = Perro(namePet,nameHuman,address,phone,baño,byc)
                nuevo_perro.cargar_perro()

                print("Perro cargado exitosamente")
                self.menu()

            # ==================== OPCION 2 ==================== 
            if nro == 2:            
                # AQUI CAPTAREMOS LOS DATOS A MODIFICAR LUEGO HAREMOS 
                # UN UPDATE DE LOS DATOS CON RESPECTO AL NOMBRE DEL CANINO
                namePet = input('nombre del firulais: ').upper() 
                address = input('nueva direción: ').upper()
                phone = input('nuevo Teléfono: ').upper()
                Perro.modificar_perro(address,phone,namePet)

                print("Perro modificado exitosamente")
                self.menu()
            # ==================== OPCION 3 ==================== 
            # Dado un nombre de un perro eliminarlo de la base de datos.
            if nro == 3:
                namePet = input('nombre del firulais: ').upper() 
                Perro.borrar_perro(namePet)

                print("Registro eliminado exitosamente")
                self.menu()
            # ==================== OPCION 4 ==================== 
            # ==================== OPCION 5 ==================== 
            # ==================== OPCION 0 ==================== 
            if nro == 0:
                flag = False

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
        conexion = Conexiones()
        conexion.abrirConexion()
        conexion.miCursor.execute("INSERT INTO PERROS VALUES('{}','{}','{}','{}','{}','{}')".format(self.nombre_perro, self.nombre_dueño, self.direccion,self.telefono,self.baño,self.bayco))
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


class Conexiones:
    
    def abrirConexion(self):
        self.miConexion = sqlite3.connect("Peluqueria")
        self.miCursor = self.miConexion.cursor()
        
    def cerrarConexion(self):
        self.miConexion.close()


            
programa = ProgramaPrincipal()
programa.menu()