f=open("salida.txt","w")
a=None
with open("message (8).txt","r") as archivo:
    for linea in archivo:
        for x in range(len(linea)):
          if linea[x]==']':
            a=x+1
            #print(a)
        #print(linea[0:a]+linea[a+1::])
        f.write(linea[0:a]+linea[a+1::])



