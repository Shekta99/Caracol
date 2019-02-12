import sys

def leer():
    return (open("matriz1.txt","r").readlines())
def dimension(lista):
    return len(lista)

def recorrer(lista,ini,dim,tempo,tempo2,tempo3,cont,rango):
    for x in (rango):
        if x==rango[0]:
            for xs in (lista[x:(x+1)]):
                tempo.extend(xs[rango[0]:((rango[len(rango)-1])+1)])
        
        
        
        if x==(rango[len(rango)-1]):
            for xs in (lista[x:(x+1)]):
                tempo2.extend(xs[rango[0]:((rango[len(rango)-1])+1)])
            tempo2.reverse()
            for xs2 in (tempo2):
                tempo.extend(xs2)
                
        elif x>rango[0] and x<=(rango[len(rango)-1]):
            for xs in (lista[x:(x+1)]):
                tempo.extend(xs[rango[len(rango)-1]])
                tempo3.extend(xs[rango[0]])
            
            
    
    if (dimension(leer())-(1*(cont+1)))>=0:
        tempo3.reverse()
        tempo.extend(tempo3)
        recorrer(leer(),(1+(1*(cont+1))),(dimension(leer())-(1*(cont+1))),tempo,temp2(),temp3(),(cont+1),rango[(cont-(cont-1)):(len(rango)-1)])

        
    if(cont==2):
        print tempo
           
def temp():
    return []

def temp2():
    return []

def temp3():
    return []
def contad():
    return 0

def ult(temp3,conta):
    temp3.extend([conta])
    if conta<(dimension(leer())-1):
        ult(temp3,conta+1)
    return temp3

def main():
    recorrer(leer(),0,(dimension(leer())),temp(),temp2(),temp3(),2,ult(temp3(),0))


main()

'''
def cargar_archivo(lab):
    return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]]
    ##return [x.split(" ") for x in [y.strip("\n") for y in open(lab).readlines()]][1][0].split(",")
'''
