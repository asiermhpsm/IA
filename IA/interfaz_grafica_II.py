# -*- coding: utf-8 -*-
"""
Created on Sun Nov 13 20:06:10 2022

@author: asier
"""

from tkinter import *

root=Tk()

miFrame=Frame(root, width=500, height=400)

miFrame.pack()

Label(miFrame, text="Hola mundo", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

miImagen=PhotoImage(file="mapa_metro_Atenas.jpg")
Label(miFrame, image=miImagen).place(x=10, y=10)


root.mainloop()