from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from cargar_personal import *
from conexiones import *
from perro import *
import sqlite3

# desarrollo interfaz grafica
root = Tk()
root.title("Peluqueria canina")
root.geometry("940x450")
#========= nuevas pestañas =========
nb = ttk.Notebook(root) 
nb.pack(fill='both',expand='yes')

perro = ttk.Frame(nb)
nb.add(perro,text='Perros')

recepcionista = ttk.Frame(nb)
nb.add(recepcionista,text='carga de recepcionista')

peluquero = ttk.Frame(nb)
nb.add(peluquero,text='carga de peluquero')
#==================================

#=========== VAR PERROS ===========
namePet = StringVar()
nameHuman = StringVar()
address = StringVar()
phone = IntVar()
bath = IntVar()
byc = IntVar()
comportamiento = StringVar()
#==================================

def conexionBBDD():

    try:
        conexion = Conexiones() 
        conexion.abrirConexion()
        conexion.crearTablas()
        messagebox.showinfo("CONEXION","Base de datos creada exitosamente")
    except:
        messagebox.showinfo("CONEXION","conexion exitosa con la base de datos")

def salir():
    valor = messagebox.askquestion("Salir","¿Esta seguro que desea salir?")
    if valor == "yes":
        root.destroy()

def limpiarCampos():
    #CAMPOS PERROS
    namePet.set("")
    nameHuman.set("") 
    address.set("") 
    phone.set("") 
    bath.set("") 
    byc.set("") 
    comportamiento.set("")

    #CAMPOS PELUQUEROS
    nombre.set("")
    apellido.set("")
    dni.set("")
    direccion.set("")
    tel.set("")
    email.set("")
    exp.set("")
    sueldo.set("")

    #CAMPOS RECEPCIONISTAS
    nombreRep.set("")
    apellidoRep.set("")
    dniRep.set("")
    direccionRep.set("")
    telRep.set("")
    emailRep.set("")
    sueldoRep.set("")

def mensaje():
    acerca = '''
    Aplicacion  Lista
    Version     1.0
    author      jig
    '''
    messagebox.showinfo(title="INFORMACIÓN", message = acerca )
#======================================= METODOS CRUD =====================================
def cargarPerro():
    try:
        nuevo_perro = Perro(namePet.get(),nameHuman.get(),address.get(),phone.get(),bath.get(),byc.get())
        nuevo_perro.cargar_perro()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al crear el registro,verifique conexion con BBDD")
        pass
    limpiarCampos()
    mostrar()

def comportamientoPerro(): 
    
    try:
        if Perro.lista_nombres_perros(namePet.get()):

            if (comportamiento.get()).lower() in ['muy bien','bien','mal','muy mal']:
                Perro.agregar_comportamiento((comportamiento.get()).lower(),namePet.get())
                mostrar()
            else:
                messagebox.showinfo("ERROR","solo ingrese 'muy bien','bien','mal' o 'muy mal' ")
        else:
            messagebox.showinfo("ERROR","El perro no existe")
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al modificar el registro")
        pass
    limpiarCampos()

def mostrar(): 
    
    registros = tree.get_children()
    for elemento in registros:
        tree.delete(elemento)
    
    try:
        records = Perro.listado_perros()
        for row in records:
            tree.insert("",0,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error ")

def actualizar():
    try:
        Perro.modificar_perro(address.get(),phone.get(),namePet.get())
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al modificar el registro")
        pass
    limpiarCampos()
    mostrar()

def borrar():
    try:
        if messagebox.askyesno(message="¿Desea eliminar el registro?",title="ADVERTENCIA"):
            Perro.borrar_perro(namePet.get())    
    except: 
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error al eliminar el registro")
        pass
    limpiarCampos()
    mostrar()

def agregarMotivo():
    try:
        if bath.get() == 1: 
            byc.set(0)
        elif byc.get() == 1: 
           byc.set(0) 
        else:
            messagebox.showinfo("ADVERTENCIA","Solo ingrese 0 o 1")    
        
        Perro.incrementar_motivo(bath.get(),byc.get(),namePet.get())
        mostrar()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error")
        
#========================================== tabla =========================================
tree = ttk.Treeview(perro,height=10, columns=('#0','#1','#2','#3','#4','#5','#6'))
tree.place(x=0,y=130)
tree.column('#0', width=10)
tree.heading('#1',text="Perro", anchor=CENTER)
tree.column('#1', width=100)
tree.heading('#2',text="Dueño", anchor=CENTER)
tree.column('#2', width=100)
tree.heading('#3',text="Direccion", anchor=CENTER)
tree.column('#3', width=100)
tree.heading('#4',text="TEL", anchor=CENTER)
tree.column('#4', width=100)
tree.heading('#5',text="Baño", anchor=CENTER)
tree.column('#5', width=100)
tree.heading('#6',text="Ba y Co", anchor=CENTER)
tree.column('#6', width=100)
tree.heading('#7',text="Comprt", anchor=CENTER)
tree.column('#7', width=100)


def seleccionar(event):
    item = tree.identify("item",event.x,event.y)
    namePet.set(tree.item(item,"values")[0])
    nameHuman.set(tree.item(item,"values")[1])
    address.set(tree.item(item,"values")[2])
    phone.set(tree.item(item,"values")[3])
    comportamiento.set(tree.item(item,"values")[6])

tree.bind("<Double-1>",seleccionar)
#==================================== MENU PRACTICA 4 =====================================
menubar = Menu(root)
menubasedat = Menu(menubar,tearoff=0)
menubasedat.add_command(label="Crear/Conectar base de datos ", command= conexionBBDD)
# menubasedat.add_command(label="Cargar visita ", command=eliminarBBDD)
menubasedat.add_command(label="Salir ", command=salir)
menubar.add_cascade(label="Inicio",menu=menubasedat)

#======================================== ETIQUETAS =======================================
l2 = Label(perro, text="Canino")
l2.place(x=50,y=10)
e2 = Entry(perro,textvariable=namePet)
e2.place(x=150,y=10)

l3 = Label(perro, text="Dueño")
l3.place(x=50,y=40)
e3 = Entry(perro,textvariable=nameHuman)
e3.place(x=150,y=40)

l4 = Label(perro, text="Direccion")
l4.place(x=50,y=70)
e4 = Entry(perro,textvariable=address, width=30)
e4.place(x=150,y=70)

l5 = Label(perro, text="Teléfono")
l5.place(x=50,y=100)
e5 = Entry(perro,textvariable=phone, width=30)
e5.place(x=150,y=100)

l6 = Label(perro, text="baño")
l6.place(x=400,y=10)
e6 = Entry(perro,textvariable=bath, width=30)
e6.place(x=500,y=10)

l7 = Label(perro, text="baño y corte")
l7.place(x=400,y=40)
e7 = Entry(perro,textvariable=byc, width=30)
e7.place(x=500,y=40)

l8 = Label(perro, text="Comportamiento")
l8.place(x=400,y=70)
e8 = Entry(perro,textvariable=comportamiento, width=30)
e8.place(x=500,y=70)
#========================= BOTONES ====================================

b1 = Button(perro,text="Agregar a lista" , command = cargarPerro)
b1.place(x = 720, y = 130)

b2 = Button(perro,text="Modificar registro" , command = actualizar)
b2.place(x = 720, y = 160)

b3 = Button(perro,text="Cambiar comportamiento" , command = comportamientoPerro)
b3.place(x = 720, y = 190)

b4 = Button(perro,text="Mostrar" , command = mostrar)
b4.place(x = 720, y = 220)

b5 = Button(perro,text="Agregar motivo" , command = agregarMotivo)
b5.place(x = 720, y = 250)

b6 = Button(perro,text="Eliminar registro" ,bg= "red", command = borrar)
b6.place(x = 720, y = 280)
root.config(menu=menubar)

###################################################################################### 
# ==================================== PELUQUEROS ====================================
###################################################################################### 

nombre = StringVar()
apellido = StringVar()
dni = IntVar()
direccion = StringVar()
tel = IntVar()
email = StringVar()
sueldo = IntVar()
exp = IntVar()
condicion = IntVar()
#======================================= FUNCIONES =======================================
def cargarPeluquero():
    try:
        peluquero1 = Peluquero(nombre.get(),apellido.get(),dni.get(),direccion.get(),tel.get(),email.get(),sueldo.get(),exp.get())
        peluquero1.cargarCodPeluquero()
        messagebox.showinfo("ÉXITO","Registro exitoso ")
        limpiarCampos()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error ")
    limpiarCampos()

def mostrarSueldos():
    try:
        registros = tree2.get_children()
        for elemento in registros:
            tree2.delete(elemento)
    
        records = Peluquero.listado_peluqueros(condicion.get())
        for row in records:
            tree2.insert("",0,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error ")

#======================================== BOTONES ========================================
b1 = Button(peluquero,text="Agregar a lista" , command = cargarPeluquero)
b1.place(x = 700, y = 10)

b2 = Button(peluquero,text="Sueldos mayores a: " , command = mostrarSueldos)
b2.place(x = 700, y = 40)

root.config(menu=menubar)
#======================================== ETIQUETAS =======================================

l3 = Label(peluquero, text="Nombre")
l3.place(x=50,y=10)
e3 = Entry(peluquero,textvariable=nombre)
e3.place(x=150,y=10)

l4 = Label(peluquero, text="Apellido")
l4.place(x=50,y=40)
e4 = Entry(peluquero,textvariable=apellido, width=30)
e4.place(x=150,y=40)

l5 = Label(peluquero, text="DNI")
l5.place(x=50,y=70)
e5 = Entry(peluquero,textvariable=dni, width=30)
e5.place(x=150,y=70)

l6 = Label(peluquero, text="Dirección")
l6.place(x=50,y=100)
e6 = Entry(peluquero,textvariable=direccion, width=30)
e6.place(x=150,y=100)

l7 = Label(peluquero, text="Teléfono")
l7.place(x=400,y=10)
e7 = Entry(peluquero,textvariable=tel, width=30)
e7.place(x=500,y=10)

l8 = Label(peluquero, text="Email")
l8.place(x=400,y=40)
e8 = Entry(peluquero,textvariable=email, width=30)
e8.place(x=500,y=40)

l9 = Label(peluquero, text="Sueldo")
l9.place(x=400,y=70)
e9 = Entry(peluquero,textvariable=sueldo, width=30)
e9.place(x=500,y=70)

l10 = Label(peluquero, text="Experiencia")
l10.place(x=400,y=100)
e10 = Entry(peluquero,textvariable=exp, width=30)
e10.place(x=500,y=100)

e11 = Entry(peluquero,textvariable=condicion, width=20)
e11.place(x=700,y=70)
# ================================= TABLA PELUQUEROS =================================
tree2 = ttk.Treeview(peluquero,height=10, columns=('#0','#1','#2','#3','#4','#5','#6','#7','#8'))
tree2.place(x=0,y=130)
tree2.column('#0', width=5)
tree2.heading('#1',text="Codigo", anchor=CENTER)
tree2.column('#1', width=100)
tree2.heading('#2',text="Nombre", anchor=CENTER)
tree2.column('#2', width=100)
tree2.heading('#3',text="Apellido", anchor=CENTER)
tree2.column('#3', width=100)
tree2.heading('#4',text="DNI", anchor=CENTER)
tree2.column('#4', width=100)
tree2.heading('#5',text="Direccion", anchor=CENTER)
tree2.column('#5', width=100)
tree2.heading('#6',text="Tel", anchor=CENTER)
tree2.column('#6', width=100)
tree2.heading('#7',text="Email", anchor=CENTER)
tree2.column('#7', width=100)
tree2.heading('#8',text="Sueldo", anchor=CENTER)
tree2.column('#8', width=100)
tree2.heading('#9',text="Experiencia", anchor=CENTER)
tree2.column('#9', width=100)

###################################################################################### 
# ================================== RECEPCIONISTAS ==================================
######################################################################################

nombreRep = StringVar()
apellidoRep = StringVar()
dniRep = IntVar()
direccionRep = StringVar()
telRep = IntVar()
emailRep = StringVar()
sueldoRep = IntVar()
#======================================= FUNCIONES =======================================
def cargarRecepcionista():
    try:
        recepcionista1 = Recepcionista(nombreRep.get(),apellidoRep.get(),dniRep.get(),direccionRep.get(),telRep.get(),emailRep.get(),sueldoRep.get())
        recepcionista1.cargarCodRecepcionista()
        messagebox.showinfo("ÉXITO","Registro exitoso ")
        limpiarCampos()
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error ")
    limpiarCampos()

def mostrarRep():
    try:
        registro = tree3.get_children()
        for elemento in registro:
            tree3.delete(elemento)
    
        records = Recepcionista.listado_recepcionistas()
        for row in records:
            tree3.insert("",0,values=(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]))
    except:
        messagebox.showwarning("ADVERTENCIA","Ocurrio un error ")
#======================================== BOTONES ========================================
b1 = Button(recepcionista,text="Agregar a lista" , command = cargarRecepcionista)
b1.place(x = 700, y = 10)

b2 = Button(recepcionista,text="Mostrar recepcionistas: " , command = mostrarRep)
b2.place(x = 700, y = 40)

root.config(menu=menubar)
#======================================== ETIQUETAS =======================================

l3 = Label(recepcionista, text="Nombre")
l3.place(x=50,y=10)
e3 = Entry(recepcionista,textvariable=nombreRep)
e3.place(x=150,y=10)

l4 = Label(recepcionista, text="Apellido")
l4.place(x=50,y=40)
e4 = Entry(recepcionista,textvariable=apellidoRep, width=30)
e4.place(x=150,y=40)

l5 = Label(recepcionista, text="DNI")
l5.place(x=50,y=70)
e5 = Entry(recepcionista,textvariable=dniRep, width=30)
e5.place(x=150,y=70)

l6 = Label(recepcionista, text="Dirección")
l6.place(x=50,y=100)
e6 = Entry(recepcionista,textvariable=direccionRep, width=30)
e6.place(x=150,y=100)

l7 = Label(recepcionista, text="Teléfono")
l7.place(x=400,y=10)
e7 = Entry(recepcionista,textvariable=telRep, width=30)
e7.place(x=500,y=10)

l8 = Label(recepcionista, text="Email")
l8.place(x=400,y=40)
e8 = Entry(recepcionista,textvariable=emailRep, width=30)
e8.place(x=500,y=40)

l9 = Label(recepcionista, text="Sueldo")
l9.place(x=400,y=70)
e9 = Entry(recepcionista,textvariable=sueldoRep, width=30)
e9.place(x=500,y=70)

# ================================= TABLA RECEPCIONISTAS =================================
tree3 = ttk.Treeview(recepcionista,height=10, columns=('#0','#1','#2','#3','#4','#5','#6','#7'))
tree3.place(x=0,y=130)
tree3.column('#0', width=5)
tree3.heading('#1',text="Codigo", anchor=CENTER)
tree3.column('#1', width=100)
tree3.heading('#2',text="Nombre", anchor=CENTER)
tree3.column('#2', width=100)
tree3.heading('#3',text="Apellido", anchor=CENTER)
tree3.column('#3', width=100)
tree3.heading('#4',text="DNI", anchor=CENTER)
tree3.column('#4', width=100)
tree3.heading('#5',text="Direccion", anchor=CENTER)
tree3.column('#5', width=100)
tree3.heading('#6',text="Tel", anchor=CENTER)
tree3.column('#6', width=100)
tree3.heading('#7',text="Email", anchor=CENTER)
tree3.column('#7', width=100)
tree3.heading('#8',text="Sueldo", anchor=CENTER)
tree3.column('#8', width=100)

root.mainloop()