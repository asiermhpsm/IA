import json
import numpy as np
import sys
from tkinter import *
from tkinter import ttk
from BusquedaAEstrella import AEstrella
from PIL import ImageTk, Image

#def display_coordinates(event):
#    label['text']=f'x={event.x} y={event.y}'

def listJson(file): #lista el fichero json dado
    with open(file,'r') as f:
        listed=json.load(f)
        f.close()
    return listed
stations=listJson("coordenadas.json")

root = Tk()
root.config(background="black")
root.title("Metro Atenas")

lista=[]
for station in stations:
    lista.append(station['Name'])

lineainicial=int()
lineaactual=int()
paradasrestantes=int()
resultado=StringVar()
cambiolinea=StringVar()
count=int()
linea1list=["Piraeus","Faliro","Moschato","Kallithea","Tavros","Petralona","Thissio","Monastiraki-Verde","Omonia-Verde","Victoria","Attiki-Verde","Aghios Nikolaos","Kato Patissia","Aghios Eleftherios","Ano Patissia","Perissos","Pefkakia","Nea Ionia","Iraklio","Irini","Neratziotissa","Maroussi","KAT","Kifissia"]
linea2list=["Aghios Dimitrios · Alexandros Panagoulis","Dafni","Aghios Ioannis","Neos Kosmos","Sygrou-Fix", "Akropoli","Syntagma-Rojo","Panepistimio", "Omonia-Rojo", "Metaxourghio","Larissa Station","Attiki-Rojo","Sepolia","Aghios Antonios"]
linea3list=["Egaleo","Eleonas","Kerameikos","Monastiraki-Azul","Syntagma-Azul","Evangelismos","Megaro Moussikis","Ambelokipi","Panormou","Katehaki","Ethniki Amyna","Holargos","Nomismatokopio","Aghia Paraskevi","Halandri","Doukissis Plakentias","Pallini","Paiania-Kantza", "Koropi","Airport"]

#Fuuncion dropdown_opened
def dropdown_opened():
    print("Lista desplegada.")
    
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
                    #messagebox.showinfo(message="Tome la linea "+str(lineainicial)+" en la parada "+path[0]+" y " + cambiolinea + " con una distancia total recorrida de "+ str(distance) + " kilómetros, en un tiempo total de " + str(time) + " minutos y con " + str(transfer) + " transbordos totales"  , title="Título")
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

            # Inicio del algoritmo para dibujar una línea sobre el camino del resultado
            a=listJson('lineas.json')
            b=np.zeros((len(path),2))
            print(len(a))
            print(len(path))
            for _ in range(0,len(path)-1):
                buscando=True
                i=0
                while(buscando) and (i<len(a)):
                    #print(_)
                    #print(len(path))
                    #print(path[_])
                    #print(a[i]['name'])
                    if(path[_] == a[i]['name']):
                        buscando=False
                        b[_][0]=(a[i]['x'])
                        b[_][1]=(a[i]['y'])
                    i=i+1
            print(len(b))
            for _ in range(1,len(b)-1):
                x1=b[_-1][0]
                y1=b[_-1][1]
                x2=b[_][0]
                y2=b[_][1]
                print(x1)
                print(y1)
                print(x2)
                print(y2)
                canvas.create_line(x1, y1, x2, y2, fill="red")
    else:
        resultado.set("ERROR INSUFICIENTES PARÁMETROS")

#ORIGEN
Label(root, text="Origen").grid(row=3,column=0)
combo1 = ttk.Combobox(
state="readonly",
values=lista,
    postcommand=dropdown_opened
)
combo1.grid(row=3, column=1)

#DESTINO
Label(root, text="Destino").grid(row=4, column=0)
combo2 = ttk.Combobox(
state="readonly",
values=lista,
    postcommand=dropdown_opened
)
combo2.grid(row=4,column=1)

#CRITERIO
Label(root, text="Criterio").grid(row=5,column=0)
combo3 = ttk.Combobox(
state="readonly",
values=["Distancia","Transbordo","Tiempo"],
    postcommand=dropdown_opened
)
combo3.grid(row=5,column=1)

#BOTON
botonBuscar=Button(root, text="Buscar",command=lambda:buscar())
botonBuscar.grid(row=6, column=0)

#Pantalla resultado
pantalla=ttk.Label(root, textvariable=resultado, wraplength=500)
pantalla.grid(row=6,column=1)
pantalla.config(background="white", justify="left")


canvas = Canvas(root, width=800, height=800, background="white")
#label = Label(bd=4, relief="solid", font="Times 22 bold", bg="white", fg="black")

#Open Image
my_image = Image.open("metro1.png")
#Resize image
resize = my_image.resize((800,800), Image.Resampling.LANCZOS)

new_image = ImageTk.PhotoImage(resize)

canvas.create_image(0,0,image=new_image,anchor=NW)
#canvas.bind('<Button-1>',display_coordinates)

canvas.grid(row=0, column=0, columnspan=3, rowspan=3)
#label.grid(row=1,column=0)

#BOTON SALIR
botonCancelar=Button(root, text="Salir", command=root.destroy)
botonCancelar.grid(row=7,column=0)

root.mainloop()