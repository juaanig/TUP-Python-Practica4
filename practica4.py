from perro import Perro

#VALIDAR TODOS LOS INGRESO DE DATOS

class ProgramaPrincipal:

    flag = True

    def menu(self):
        try:
            while self.flag:
                try:
                    print('____________________________________\n')
                    print('\tMENÚ\n1- Cargar Perros.\n2- Modificar datos de un perro.\n3- Borrar un perro.\n4- Cargar visita.\n5- Listado de Perros.\n0- Salir del menú.')
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
                        opcion=input('Desea modificar el comportamiento? Presione Y para continuar o cualquier otra tecla para salir.').upper()
                        if opcion == 'Y':
                            nuevoPerro=input('Ingrese el nombre del perro: ').upper()
                            #validar si existe el perro
                            nuevoComportamiento=input('Ingrese el nuevo comportamiento: ')
                            #if nuevoComportamiento

                            Perro.agregar_comportamiento(nuevoComportamiento,nuevoPerro)  

                        self.menu()
                except:
                    print('Error en opción 5')
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