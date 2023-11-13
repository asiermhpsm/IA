import json
import networkx as nx
from math import sin, cos, atan2, sqrt, radians

def listJson(file): #lista el fichero json dado
    with open(file,'r') as f:
        listed=json.load(f)
        f.close()
    return listed

class AEstrella:
    def __init__(self,root,goal,criteria):
        super().__init__
        self.root=root #origen
        self.goal=goal #destino
        self.criteria=criteria #criterio de búsqueda (por distancia,tiempo,transbordos)
        self.opened=[] #lista abierta
        self.closed=[] #lista cerrada
        self.node=None #nodo en el que nos encontramos en cada instante
        self.path=[] #camino optimo segun el criterio desde el origen hasta el destino
        self.distance=0 #distancia del recorrido
        self.time=0 #tiempo de trayecto
        self.transfers=0 #numero de transbordos del trayecto
        self.g=nx.Graph()
        stations=listJson('coordenadas.json')
        for station in stations:
            self.g.add_node(station['Name'])
            self.g.nodes[station['Name']]['Lat']=station['Lat']
            self.g.nodes[station['Name']]['Lon']=station['Lon']
        edges=listJson('aristas.json')
        lista=[[0 for column in range(0,3)] for row in range(0,len(edges))]
        i=0
        for edge in edges:
            lista[i][0]=edge['Origen']
            lista[i][1]=edge['Destino']
            lista[i][2]=edge['Peso'][self.criteria]
            i+=1
        self.g.add_weighted_edges_from(lista)
        self.g.nodes[self.root]['G']=0

    def estimateH(self,son): #formula de Haversine que permite calcular la distancia en linea recta entre son y goal que es una estimacion de h
        R=6371.0 #radio medio de La Tierra
        latSon=radians(self.g.nodes[son]['Lat']) #pasamos las coordenadas a radianes
        lonSon=radians(self.g.nodes[son]['Lon'])
        latGoal=radians(self.g.nodes[self.goal]['Lat'])
        lonGoal=radians(self.g.nodes[self.goal]['Lon'])
        deltaLat=latGoal-latSon
        deltaLon=lonGoal-lonSon
        a=sin(deltaLat/2)**2+cos(latSon)*cos(latGoal)*sin(deltaLon/2)**2
        c=2*atan2(sqrt(a),sqrt(1-a))
        return R*c
    
    def estimateF(self,father,son):
        g=self.g.edges[father,son]['weight']
        h=self.estimateH(son)
        self.g.nodes[son]['G']=self.g.nodes[father]['G']+g #el valor de g es el peso acumulado segun el criterio seleccionado
        self.g.nodes[son]['F']=self.g.nodes[son]['G']+h #el valor de f=g+h
    
    def minimum(self): #ordena la lista abierta de menor a mayor valor de F
        min=self.opened[0]
        if(len(self.opened)>1):
            for i in self.opened:
                if(self.g.nodes[i]['F']<self.g.nodes[min]['F']):
                    min=i
        self.opened.remove(min)
        return min

    def algorithm(self):
        self.opened.append(self.root) #introducimos el origen en la lista abierta
        found=False
        while(len(self.opened)>0 and found!=True): #si la lista abierta no esta vacia y no hemos encontrado la meta continuamos
            self.node=self.minimum()
            self.closed.append(self.node)
            if(self.node==self.goal): #si el nodo que sacamos de abierta es meta entonces terminamos
                found=True
                self.opened.clear()
            else:
                neighbors=self.g[self.node] #sacamos los nodos adyacentes al actual
                for neighbor in neighbors:
                    if(self.opened.count(neighbor)==0 and self.closed.count(neighbor)==0): 
                        self.estimateF(self.node,neighbor) #calculamos el valor de F
                        self.g.nodes[neighbor]['Father']=self.node #apuntamos al nodo actual
                        self.opened.append(neighbor) #introducimos el nodo en la lista abierta

                    elif(self.opened.count(neighbor)>0):
                        if(self.g.nodes[neighbor]['G']>self.g.nodes[self.node]['G']+self.g.edges[self.node,neighbor]['weight']):
                            self.estimateF(self.node,neighbor)
                            self.g.nodes[neighbor]['Father']=self.node
        if (found==True): 
            while(self.node!=self.root):
                self.path.append(self.node)
                self.node=self.g.nodes[self.node]['Father']
            self.path.append(self.node)
            self.path.reverse()
        
        edges=listJson('aristas.json')
        actual=None
        next=None        
        for i in range(len(self.path)-1):
            actual=self.path[i]
            next=self.path[i+1]
            for edge in edges:
                if((edge['Origen']==actual and edge['Destino']==next) or (edge['Origen']==next and edge['Destino']==actual)):
                    self.distance+=edge['Peso']['Distancia']
                    self.time+=edge['Peso']['Tiempo']
                    self.transfers+=edge['Peso']['Transbordo']
        
        return self.path,self.distance,self.time,self.transfers
