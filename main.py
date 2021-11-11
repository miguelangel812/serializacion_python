from tkinter import *
from tkinter.ttk import *
from tkinter.ttk import Combobox

#from dataclasses import dataclass


lista = []
def guardar():
    iden = id_sv.get()
    nombre = nombre_sv.get()
    nac = nacionalidad_sv.get()
    eq = equipo_sv.get()
    dor = dorsal_sv.get()
    pos = posicion_sv.get()

    lista.append(iden + "$" + nombre + "$" + nac + "$" + eq+ "$" + dor + "$" + pos)
    guardarJugador()
    iden = id_sv.set("")
    nombre = nombre_sv.set("")
    nac = nacionalidad_sv.set("")
    eq = equipo_sv.set("")
    dor = dorsal_sv.set("")
    pos = posicion_sv.set("")
    mostrar()

def modificar_jugador():
    eliminar.get()
    for elemento in lista:
        lista_eliminar = elemento.split("$")
        if eliminar.get() == lista_eliminar[0]:
            lista.remove(elemento)
    guardarJugador()
    guardar()


def eliminar_jugador():
    eliminar.get()
    for elemento in lista:
        lista_eliminar = elemento.split("$")
        if eliminar.get() == lista_eliminar[0]:
            lista.remove(elemento)
    guardarJugador()
    iden = id_sv.set("")
    nombre = nombre_sv.set("")
    nac = nacionalidad_sv.set("")
    eq = equipo_sv.set("")
    dor = dorsal_sv.set("")
    pos = posicion_sv.set("")
    mostrar()


def mostrar():
    r = Text(ventana, x=50, y=260, width=530, height=220)
    lista.sort()
    valores = []
    r.insert(INSERT, "ID\tNombre\tNacionalidad\t\tEquipo\t\tDorsal\tPosicion\n")
    for elemento in lista:
        lista_mostrar = elemento.split("$")
        valores.append(lista_mostrar[0])
        r.insert(INSERT, lista_mostrar[0] + "\t" + lista_mostrar[1] + "\t" + lista_mostrar[2] + "\t\t" + lista_mostrar[3]+ "\t\t" + lista_mostrar[4]+ "\t" + lista_mostrar[5] + "\n")
        r.place(x=50, y=260, width=530, height=220)
        spin_eliminar = Combobox(ventana, value=(valores), textvariable=eliminar)
        spin_eliminar.place(x=450, y=50)
    if lista == []:
        spin_eliminar = Combobox(ventana, value=(valores))
        spin_eliminar.place(x=450, y=50)
    r.config(state=DISABLED)


def iniciarArchivo():
    archivo = open("jugadores.txt", "a")
    archivo.close()


def cargar():
    archivo = open("jugadores.txt", "r")
    linea = archivo.readline()
    if linea:
        while linea:
            if linea[-1] == "\n":
                linea = linea[:-1]
            lista.append(linea)
            linea = archivo.readline()
    archivo.close()


def guardarJugador():
    archivo = open("jugadores.txt", "w")
    lista.sort()
    for elemento in lista:
        archivo.write(elemento + "\n")
    archivo.close()
#Creacion del JFrame y dandole un tamaño y la imposibilidad de expansión


ventana = Tk()
ventana.title("APLICACION LUÍS")
ventana.geometry("620x500")
ventana.resizable(width=False, height=False)

id_sv = StringVar()
nombre_sv = StringVar()
nacionalidad_sv = StringVar()
dorsal_sv = StringVar()
equipo_sv = StringVar()
posicion_sv = StringVar()
eliminar = StringVar()

iniciarArchivo()
cargar()
mostrar()
#eliminar


#Titulo de la pantalla y tamaño
titulo = Label(ventana,text ="Jugadores de Fútbol")
titulo.place(x=270,y=10)


#Etiqueta ID, El entry es para guardar la información en una variable
e_id = Label(ventana,text="ID")
e_id.place(x=50,y=50)
i_id = Entry(ventana, textvariable = id_sv)
i_id.place(x=150,y=50)
#Etiqueta Nombre, El entry es para guardar la información en una variable
e_nombre = Label(ventana,text="Nombre")
e_nombre.place(x=50,y=80)
i_nombre = Entry(ventana, textvariable = nombre_sv)
i_nombre.place(x=150,y=80)
#Etiqueta Nacionalidad, El entry es para guardar la información en una variable
e_nacionalidad = Label(ventana,text="Nacionalidad")
e_nacionalidad.place(x=50,y=140)
i_nacionalidad = Entry(ventana, textvariable = nacionalidad_sv)
i_nacionalidad.place(x=150,y=140)
#Etiqueta Dorsal, El entry es para guardar la información en una variable
e_dorsal = Label(ventana,text="Dorsal")
e_dorsal.place(x=50,y=170)
combobox_dorsal = Combobox(ventana, textvariable=dorsal_sv)
combobox_dorsal['values']= (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30)
combobox_dorsal.place(x=150,y=170)
#i_dorsal = Entry(ventana, textvariable = dorsal_sv)
#i_dorsal.place(x=150,y=170)
#Etiqueta Equipo, El entry es para guardar la información en una variable
e_equipo = Label(ventana,text="Equipo")
e_equipo.place(x=50,y=110)
i_equipo = Entry(ventana, textvariable = equipo_sv)
i_equipo.place(x=150,y=110)
#Etiqueta Posicion, El entry es para guardar la información en una variable
e_posicion = Label(ventana,text="Posicion")
e_posicion.place(x=50,y=200)
combobox_dorsal = Combobox(ventana, textvariable=posicion_sv)
combobox_dorsal['values']= ('POR','CAD','LTD','DFC','LTI','CAI','MCD','MD','MC','MI','MCO','SDD','MP','SDI','ED','DC','EI')
combobox_dorsal.place(x=150,y=200)
#i_posicion = Entry(ventana, textvariable = posicion_sv)
#i_posicion.place(x=150,y=200)
#Etiqueta Eliminar, El entry es para guardar la información en una variable
e_eliminar = Label(ventana,text="ID")
e_eliminar.place(x=370,y=50)
spin_eliminar = Combobox(ventana,text = eliminar)
spin_eliminar.place(x=450,y=50)


#Botón para guardar la información
b_guardar = Button(ventana, text="Guardar", command = guardar)
b_guardar.place(x=50,y=230)
#Botón eliminar
b_eliminar = Button(ventana,text = "Eliminar",command = eliminar_jugador)
b_eliminar.place(x=125,y=230)
#Botón modificar información
b_modificar = Button(ventana,text = "Modificar",command = modificar_jugador)
b_modificar.place(x=200,y=230)
#Botón Ver información
b_ver = Button(ventana,text = "Ver Jugadores",command = mostrar)
b_ver.place(x=275,y=230)


ventana.mainloop()