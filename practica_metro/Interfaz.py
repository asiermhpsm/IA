# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 20:28:32 2022
@author: asier
"""
import json
import sys
from tkinter import *
from tkinter import ttk
from BusquedaAEstrella import AEstrella
from tkinter import messagebox
def listJson(file): #lista el fichero json dado
    with open(file,'r') as f:
        listed=json.load(f)
        f.close()
    return listed
stations=listJson("coordenadas.json")

lista=[]
for station in stations:
    lista.append(station['Name'])

lineainicial=int()
lineaactual=int()
paradasrestantes=int()
raiz = Tk()
resultado=StringVar()
cambiolinea=StringVar()
count=int()
raiz.geometry("1200x700")
linea1list=["Piraeus","Faliro","Moschato","Kallithea","Tavros","Petralona","Thissio","Monastiraki-Verde","Omonia-Verde","Victoria","Attiki-Verde","Aghios Nikolaos","Kato Patissia","Aghios Eleftherios","Ano Patissia","Perissos","Pefkakia","Nea Ionia","Iraklio","Irini","Neratziotissa","Maroussi","KAT","Kifissia"]
linea2list=["Aghios Dimitrios · Alexandros Panagoulis","Dafni","Aghios Ioannis","Neos Kosmos","Sygrou-Fix", "Akropoli","Syntagma-Rojo","Panepistimio", "Omonia-Rojo", "Metaxourghio","Larissa Station","Attiki-Rojo","Sepolia","Aghios Antonios"]
linea3list=["Egaleo","Eleonas","Kerameikos","Monastiraki-Azul","Syntagma-Azul","Evangelismos","Megaro Moussikis","Ambelokipi","Panormou","Katehaki","Ethniki Amyna","Holargos","Nomismatokopio","Aghia Paraskevi","Halandri","Doukissis Plakentias","Pallini","Paiania-Kantza", "Koropi","Airport"]

raiz.title("Metro Atenas")
#FRAME BOTONES
frameBotones=Frame(raiz, width=561, height=350)
frameBotones.pack(side="left", anchor="n", padx = 10, pady = 10)
#Pantalla resultado


pantalla=Entry(frameBotones,textvariable=resultado)
pantalla.place(x=40, y=250,height=100,width=1000)

pantalla.config(background="white",fg="black", justify="left")
#Fuuncion dropdown_opened
def dropdown_opened():
    print("Lista desplegada.")
#ESTADO INICIAL
#Funcion pertenece
def pertenece(estacion):
    global lineainicial
    if(estacion in linea1list ):
        return 1
    elif(estacion in linea2list):
        return 2
    else:
        return 3

#Funcion Buscar
def buscar():
    global resultado
    global count
    global cambiolinea
    if combo1.get()!="" and combo2.get()!="" and combo3.get()!="" :
        if combo1.get()==combo2.get():
            resultado.set("MISMA PARADA ORIGEN Y DESTINO")
        else:

            A=AEstrella(combo1.get(),combo2.get(),combo3.get())
            path,distance,time,transfer=A.algorithm()
            combo1.set("")
            combo2.set("")
            combo3.set("")
            n=len(path)
            nf=str(n-1)
            lineainicial=pertenece(path[0])
            lineaactual=lineainicial
            paradasrestantes=n
            cambiolinea=""
            i=0
            while(i<n):
                if(i==n-1):
                    cambiolinea+=" continua " + str(paradasrestantes-1) + " paradas hasta llegar a " + str(path[i])
                    i=i+1
                    resultado.set("Tome la linea "+str(lineainicial)+" en la parada "+path[0]+" y " + cambiolinea + " con una distancia total recorrida de "+ str(distance) + "en un tiempo total de " + str(time) + " y con " + str(transfer) + "transbordos totales" )
                    messagebox.showinfo(message="Tome la linea "+str(lineainicial)+" en la parada "+path[0]+" y " + cambiolinea + " con una distancia total recorrida de "+ str(distance) + " kilómetros, en un tiempo total de " + str(time) + " minutos y con " + str(transfer) + " transbordos totales"  , title="Título")
                elif (lineaactual!=pertenece(path[i]) and count==0):
                    lineaactual=pertenece(path[i])
                    cambiolinea=",tras " +str(i-1) + " paradas, cambie en la estacion "+ str(path[i]) + " a la linea " + str(lineaactual)
                    count=1
                    paradasrestantes=n-i
                    i=i+1
                elif(lineaactual!=pertenece(path[i]) and count!=0 ):
                    lineaactual=pertenece(path[i])
                    cambiolinea+=" vuelva a cambiar tras " + str(i-paradasrestantes) + " paradas, en la estacion " + str(path[i]) +  " ,a la linea "+ str(lineaactual)
                    paradasrestantes=n-i
                    i=i+1

                else:
                    i=i+1





        #Label(frameBotones, text=A.algorithm()).place(x=40, y=250)
    else:
        resultado.set("ERROR INSUFICIENTES PARÁMETROS")


#raiz.iconbitmap("Athens_Metro_Logo.ico")

frameImagen=Frame(raiz, width=639, height=700)
frameImagen.pack(side="right", padx = 10, pady = 10)

#IMAGEN
miImagen=PhotoImage(file="metro.png")
Label(frameImagen, image=miImagen).place(x=10, y=10)




#ORIGEN
Label(frameBotones, text="Origen").place(x=40, y=40)
combo1 = ttk.Combobox(
state="readonly",
values=lista,
    postcommand=dropdown_opened
)
combo1.place(x=125, y=50)

#DESTINO
Label(frameBotones, text="Destino").place(x=40, y=90)
combo2 = ttk.Combobox(
state="readonly",
values=lista,
    postcommand=dropdown_opened
)
combo2.place(x=125, y=100)

#CRITERIO
Label(frameBotones, text="Criterio").place(x=40, y=140)
combo3 = ttk.Combobox(
state="readonly",
values=["Distancia","Transbordo","Tiempo"],
    postcommand=dropdown_opened
)
combo3.place(x=125, y=150)

#BOTON
botonBuscar=Button(frameBotones, text="Buscar",command=lambda:buscar())
botonBuscar.place(x=40, y=190)

#BOTON SALIR
botonCancelar=Button(raiz, text="Salir", command=raiz.destroy)
botonCancelar.place(x=300, y=300)

#frameRes=Frame(raiz, width=561, height=350)
#frameRes.pack(side="left", anchor="s", padx = 10, pady = 10)


#LISTA PARADAS
#Label(frameBotones, text=resultado).place(x=40, y=250)



raiz.mainloop()
