# Bibliotecas
import random

class Adaline:
    
    def _init_(self):
        self.data=[[]]

    def leer_data_excel(self):
        self.data=[
            [0,0,1,1],
            [0,1,0,2],
            [0,1,1,3],
            [1,0,0,4],
            [1,0,1,5],
            [1,1,0,6],
            [1,1,1,7]
            ]
                
    def Y(self,entradas,pesos): #Salida de la red
        s=0
        for i in range(len(pesos)):
            s=s+(entradas[i]*pesos[i])
        return s

    def E(self,dp,yp): #Diferencia
        return round(dp-yp,3)

    def changue_wight(self,w,alpha,e,x): #Cambiar el peso actual
        return round((w+alpha*e*x),3)

    def entrenar(self):
        #pesos=[round(random.random(),3) for _ in range(20)]
        pesos=[0.84,0.394,0.783]
        alpha=0.3 #Valor para el umbral
        for i in range(len(self.data)):
            dp=self.data[i][3] # Valor esperado
            da=self.data[i] #Toda la fila
            y=self.Y(da,pesos) # Calcula la salida de la red
            e=self.E(dp,y) #Obtiene la diferencia entre el valor esperado y la salidad real
            print("POS ",i)
            for j in range(len(pesos)):
                print(pesos[j])
                pesos[j]=round(self.changue_wight(pesos[j],alpha,e,self.data[i][j]),3) # Actualiza el peso
                                    
        return pesos #retorna los pesos

def main():
    #Adaline
    objAdeline=Adaline()
    
    objAdeline.leer_data_excel()
    pesos_final=objAdeline.entrenar()
    print(pesos_final)


main()


