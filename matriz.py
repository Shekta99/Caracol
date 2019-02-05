import sys

def leer():
    return (open("matriz1.txt","r").readlines())
def dimension(lista):
    return len(lista)

def recorrer(lista,ini,dim,tempo,tempo2,cont):
    for x in range(ini,dim):
        if x==0:
            for xs in (lista[x:(x+1)]):
                tempo.extend(xs)
        if x==(dim-1):
            for xs in (lista[x:(x+1)]):
                tempo2.extend(xs)
            tempo2.reverse()
            for xs2 in (tempo2):
                tempo.extend(xs2)
    for j in range(ini,((dim*4)-4)):
        print tempo[j:(j+1)]
    if (dimension(leer())-(2*cont))>=0:
        recorrer(leer(),(1+(1*cont)),(dimension(leer())-(2*cont)),temp(),temp2(),(cont+1))
    
           
def temp():
    return []

def temp2():
    return []

def ult(temp3):
    return temp3.reverse()

def main():
    recorrer(leer(),0,(dimension(leer())),temp(),temp2(),2)


main()

'''
def cargar_archivo(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]]
    ##return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][1][0].split(",")
'''
