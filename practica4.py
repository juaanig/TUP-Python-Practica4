from perro import Perro
from cargar_personal import *

#VALIDAR TODOS LOS INGRESO DE DATOS

class ProgramaPrincipal:

    flag = True

    def menu(self):
        try:
            while self.flag:
                try:
                    print('____________________________________\n')
                    print('\tMENÚ\n1- Cargar Perros.\n2- Modificar datos de un perro.\n3- Borrar un perro.\n4- Cargar visita.\n5- Listado de Perros.\n6- Cargar personal\n7- Listado peluqueros\n0- Salir del menú.')
                    print('____________________________________')
                    nro = int(input("\nPor favor ingrese un número: "))
                except:
                    print('Error en ingreso de número')
                    self.menu()
                # ==================== OPCION 1 ====================
                #CARGA DE PERROS
                try:
                    if nro == 1:
                        baño = 0
                        byc = 0
                        namePet = input('nombre del firulais: ').upper()
                        nameHuman = input('nombre del humano: ').upper()
                        address = input('direción: ').upper()
                        phone = int(input('Teléfono: '))
                        #______________________________________________________
                        selector = int(input('Motivo de la visita:\n 1-Baño\n 0-Baño y Corte\ningrese un numero:'))
                        if selector == 1: baño = 1 
                        elif selector == 0: byc = 1 
                        #______________________________________________________
                        #VALIDAR QUE EL NOMBRE EXISTA
                        
                        nuevo_perro = Perro(namePet,nameHuman,address,phone,baño,byc)
                        nuevo_perro.cargar_perro()

                        print("Perro cargado exitosamente")
                        self.menu()
                except:
                    print('Error en opción 1')
                    self.menu()
                # ==================== OPCION 2 ====================
                # AQUI CAPTAREMOS LOS DATOS A MODIFICAR LUEGO HAREMOS 
                # UN UPDATE DE LOS DATOS CON RESPECTO AL NOMBRE DEL CANINO
                try: 
                    if nro == 2:            
                        namePet = input('nombre del firulais: ').upper() 
                        address = input('nueva direción: ').upper()
                        phone = int(input('nuevo Teléfono: '))
                        Perro.modificar_perro(address,phone,namePet)
                        #VALIDAR QUE EL NOMBRE EXISTA

                        print("Perro modificado exitosamente")
                        self.menu()
                except:
                    print('Error en opción 2')
                    self.menu()
                # ==================== OPCION 3 ==================== 
                # DADO EL NOMBRE DE UN PERRO ELIMINARLO DEL REGISTRO.
                try:
                    if nro == 3:
                        namePet = input('nombre del firulais: ').upper() 
                        Perro.borrar_perro(namePet)

                        print("Registro eliminado exitosamente")
                        self.menu()
                except:
                    print('Error en opción 3')
                    self.menu()
                # ==================== OPCION 4 ====================
                # LEER EL MOTIVO POR EL QUE VINO EL PERRO (Baño o baño y corte) Y AUMENTAR EN UNO LAS VARIABLES INDICADAS.
                # BUSCAR POR NOMBRE, VER POR QUE MOTIVO HA VENIDO Y AUMENTAR LAS VARIABLES
                try:
                    if nro == 4:
                        namePet = input('nombre del firulais: ').upper() 
                        Perro.seleccionar_perro(namePet)
                        motivo = int(input('Motivo :\n 1-Baño\n 0-Baño y Corte\ningrese un numero:'))
                        bañ = 1 if motivo == 1 else 0
                        bayco = 1 if motivo == 0 else 0
                        Perro.incrementar_motivo(bañ,bayco,namePet)

                        self.menu()
                except:
                    print('Error en opción 4')
                    self.menu()
                # ==================== OPCION 5 ====================
                #LISTADO DE CANINOS
                try:
                    if nro == 5:

                        Perro.listado_perros()
                        opcion=input('\n¿Desea modificar el comportamiento?\nPresione Y para continuar o cualquier otra tecla para salir: ').upper()
                        
                        if opcion == 'Y':
                            nuevoPerro=input('Ingrese el nombre del perro: ').upper()
                            
                            if Perro.lista_nombres_perros(nuevoPerro):
                                nuevoComportamiento=str(input('Ingrese el nuevo comportamiento: ')).lower() 

                                if nuevoComportamiento in ['muy bien','bien','mal','muy mal']:
                                    Perro.agregar_comportamiento(nuevoComportamiento,nuevoPerro)  
                                else:
                                    print('El comportamiento ingresado no es válido')

                            self.menu()
                except:
                    print('Error en opción 5')
                    self.menu()
                # ==================== OPCION 6 ====================
                #CARGAR PERSONAL
                try:
                    if nro == 6:
                        
                        bandera = True
                        while bandera:
                            print("Seleccione una opción:\n1-Peluquero\n2-Recepcionista\n3-Salir")
                            seleccion=int(input("Seleccione una opción: "))

                            if seleccion == 1:
                                name = input('nombre: ').upper()
                                lastname = input('apellido: ').upper()
                                dni = int(input('dni: '))
                                address = input('dirección: ').upper()
                                phone = int(input('Teléfono: '))
                                email=str(input('email: ')).upper()
                                experience=int(input('experiencia: '))
                                sueldo=int(input('sueldo: '))

                                peluquero1 = Peluquero(name,lastname,dni,address,phone,email,experience,sueldo)
                                peluquero1.crearCod()
                                peluquero1.cargarCodPeluquero()
    
                            elif seleccion == 2:
                                name = input('nombre: ').upper()
                                lastname = input('apellido: ').upper()
                                dni = int(input('dni: '))
                                address = input('dirección: ').upper()
                                phone = int(input('Teléfono: '))
                                email=str(input('email: ')).upper()
                                sueldo=int(input('sueldo: '))

                                recepcionista1= Recepcionista(name,lastname,dni,address,phone,email,sueldo)
                                recepcionista1.crearCod()
                                recepcionista1.cargarCodRecepcionista()

                            elif seleccion == 3:
                                bandera = False
                            else:
                                print('Numero invalido')
                except:
                    print('Error en opción 6')
                    self.menu()
                # ==================== OPCION 7 ====================
                #LISTADO DE PELUQUEROS
                try:
                    if nro == 7:
                        monto= int(input('Ingrese un monto: '))
                        Peluquero.listado_peluqueros(monto)
                except:
                    print('Error en opción 7')
                    self.menu()

                # ==================== OPCION 0 ====================
                 #SALIDA DEL MENU
                try:
                    if nro == 0:
                        self.flag = False
                except:
                    break
        except:
            print('* Error ejecucion de metodo menú *')
            self.menu()  
    
                
programa = ProgramaPrincipal()
programa.menu()