import numpy as np
class SOM:
    def __init__(self):
        self.entradas=[[]]
        self.pesos=[[]]
    def generarEntradas(self):
        return [[1,1,0,0],
                [0,0,0,1],
                [1,0,0,0],
                [0,0,1,1]]
    def generarPesos(self):
        return [[0.2,0.8],
                [0.6,0.4],
                [0.5,0.7],
                [0.9,0.3]]
    def asignar(self):
        self.entradas=self.generarEntradas()
        self.pesos=self.generarPesos()
    def getEntradas(self):
        return self.entradas
    def getPesos(self):
        return self.entradas
    def calcularSimilitud(self,entrada,peso):
        s=0
        for i in range(len(entrada)): #[1,2,3,4]
            s=s+pow((entrada[i]-peso[i]),2)
        return s
    def actualizarPeso(self,w,x):
        return (w+0.6*(x-w))
    def actualizarPesos(self,pos,filaX):
        for i in range(len(self.pesos)):
            value=self.pesos[i][pos]
            result=self.actualizarPeso(value,filaX[i])
            self.pesos[i][pos]= round(result,3)
    def algoritmo(self):
        eleccion=0
        n=0
        while n!=100:
            for i in range(len(self.entradas)):
                peso=np.transpose(self.pesos)
                fila=self.entradas[i]
                d1=self.calcularSimilitud(fila,peso[0])
                d2=self.calcularSimilitud(fila,peso[1])
                #Compare
                if(d1<d2): #d1 
                    eleccion=0
                else:
                    eleccion=1
                self.actualizarPesos(eleccion,fila)
                #print("Iteracion",i," (",fila,")")
            print("Iteracion ",n)
            n=n+1
        for j in self.pesos: 
            print(j)
        lista=[]
        for i in self.entradas:
            peso=np.transpose(self.pesos)
            d1=self.calcularSimilitud(i,peso[0])
            d2=self.calcularSimilitud(i,peso[1])
            if(d1<d2): #d1 
                eleccion=1
            else:
                eleccion=2
            lista.append(eleccion)
        print(lista)
objSOM=SOM()
objSOM.asignar()
objSOM.algoritmo()
