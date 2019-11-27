matriz=[
    [-1,-1,-1],
    [1,-1,-1],
    [-1,1,-1],
    [1,1,1]
    ]
def F (w1,x1,w2,x2,teta):
    return (w1*x1+w2*x2+teta)
def Y (F):
    if(F>0):
        return 1
    else:
        return -1
def change_wight(w,dx,x):
    return (w+dx*x)
def change_teta(teta,dx):
    return teta+dx
def main():
    w1=1
    w2=1
    teta=0.5
    for fila in matriz:
        x1=fila[0]
        x2=fila[1]
        AND=fila[2]
        while(Y(F(w1,x1,w2,x2,teta))!=AND):
            w1=change_wight(w1,AND,x1)
            w2=change_wight(w2,AND,x2)
            teta=change_teta(teta,AND)
            
    print("FIINAL w1: ",w1)
    print("FINAL w2: ",w2)
    print("FINAL teta: ",teta)
    


main()