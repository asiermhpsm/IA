# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 20:28:32 2022

@author: asier
"""

from tkinter import *
from tkinter import ttk

raiz = Tk()

raiz.geometry("1200x700")

raiz.title("Metro Atenas")

raiz.iconbitmap("Athens_Metro_Logo.ico")

frameImagen=Frame(raiz, width=639, height=700)
frameImagen.pack(side="right", padx = 10, pady = 10)

#IMAGEN
miImagen=PhotoImage(file="metro.png")
Label(frameImagen, image=miImagen).place(x=10, y=10)


#FRAME BOTONES
frameBotones=Frame(raiz, width=561, height=350)
frameBotones.pack(side="left", anchor="n", padx = 10, pady = 10)

#ORIGEN
Label(frameBotones, text="Origen").place(x=40, y=40)
combo = ttk.Combobox()
combo.place(x=125, y=50)

#DESTINO
Label(frameBotones, text="Destino").place(x=40, y=90)
combo = ttk.Combobox()
combo.place(x=125, y=100)

#CRITERIO
Label(frameBotones, text="Criterio").place(x=40, y=140)
combo = ttk.Combobox()
combo.place(x=125, y=150)

#BOTON
botonBuscar=Button(frameBotones, text="Buscar")
botonBuscar.place(x=40, y=190)

#FRAME RESULTADO
frameRes=Frame(raiz, width=561, height=350)
frameRes.pack(side="left", anchor="s", padx = 10, pady = 10)


#LISTA PARADAS
Label(frameBotones, text="Origen").place(x=40, y=40)







raiz.mainloop()