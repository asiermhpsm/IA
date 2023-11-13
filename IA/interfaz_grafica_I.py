# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 19:07:51 2022

@author: asier
"""

from tkinter import *

raiz = Tk()

#titulo
raiz.title("Metro Atenas")

#permitir cambiar ancho y largo de ventana
raiz.resizable(True,True)

#logotipo
raiz.iconbitmap("Athens_Metro_Logo.ico")

#tamaño ventana inicialmente
#raiz.geometry("650x350")

#cambiar color fondo
raiz.config(bg="white")

#FRAME
#creo frame
miFrame = Frame()

#empaqueto frame a la derecha y arriba(norte), si quiero q se adapte miFrame.pack(fill="par", expand="True") con par=x, y o both
miFrame.pack(side="right", anchor="n")

#cambio color de frame
miFrame.config(bg="black")

#cambio tamaño de frame (quito tamaño de raiz, esta siempre se adapta a los frame)
miFrame.config(width="650", height="350")

#cambiar borde (groove, sunken)
miFrame.config(bd=35)
miFrame.config(relief="groove")

#cambiar cursor en frame
miFrame.config(cursor="hand2")

raiz.mainloop()





















