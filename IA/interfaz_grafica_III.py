# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 21:11:36 2022

@author: asier
"""

from tkinter import *

root=Tk()

miFrame=Frame(root, width=1200, height=600)
miFrame.pack()

minombre=StringVar()

cuadroNombre=Entry(miFrame, textvariable=minombre)
cuadroNombre.grid(row=0, column=1, padx=10, pady=5)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(miFrame)
cuadroApellido.grid(row=1, column=1, padx=10, pady=5)
cuadroApellido.config(fg="red", justify="right")

cuadroDireccion=Entry(miFrame)
cuadroDireccion.grid(row=2, column=1, padx=10, pady=5)
cuadroApellido.config(fg="red", justify="right")

cuadroPassw=Entry(miFrame)
cuadroPassw.grid(row=3, column=1, padx=10, pady=5)
cuadroPassw.config(show="*")

textoComentario=Text(miFrame, width=16, height=5)
textoComentario.grid(row=4, column=1, padx=10, pady=5)

scrollVert=Scrollbar(miFrame, command=textoComentario.yview)
scrollVert.grid(row=4, column=2, sticky="nsew")

textoComentario.config(yscrollcommand=scrollVert.set)



nombreLabel=Label(miFrame, text="Nombre:")
nombreLabel.grid(row=0, column=0, sticky="w", padx=10, pady=5)

apellidoLabel=Label(miFrame, text="Apellido:")
apellidoLabel.grid(row=1, column=0, sticky="w", padx=10, pady=5)

direccionLabel=Label(miFrame, text="Direccion:")
direccionLabel.grid(row=2, column=0, sticky="w", padx=10, pady=5)

passwLabel=Label(miFrame, text="Contraseña:")
passwLabel.grid(row=3, column=0, sticky="w", padx=10, pady=5)

comentariosLabel=Label(miFrame, text="Comentarios:")
comentariosLabel.grid(row=4, column=0, sticky="w", padx=10, pady=5)



def codigoBoton():
    minombre.set("Asier")

botonEnvio=Button(root, text="Enviar", command=codigoBoton)
botonEnvio.pack()




root.mainloop()