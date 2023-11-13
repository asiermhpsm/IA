import sys
from BusquedaAEstrella import AEstrella
import random
import json

def listJson(file): #lista el fichero json dado
    with open(file,'r') as f:
        listed=json.load(f)
        f.close()
    return listed

estaciones=[]
nodes=listJson('coordenadas.json')
for station in nodes:
    estaciones.append(station['Name'])

criterios=['Tiempo','Distancia','Transbordo']
origen=random.choice(estaciones)
destino=random.choice(estaciones)
criterio=random.choice(criterios)
if(origen!=destino):
    A=AEstrella(origen,destino,criterio)
    print("Origen:"+origen+"\n")
    print("Destino:"+destino+"\n")
    print("Criterio:"+criterio+"\n")
    path,distance,time,transfer=A.algorithm()
    print("Camino:")
    print(path)
    print("Distancia:")
    print(distance)
    print("Tiempo:")
    print(time)
    print("Transbordos:")
    print(transfer)

