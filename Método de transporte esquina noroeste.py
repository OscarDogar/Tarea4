import numpy as np
'''costos = [[8,6,10,9],[9,12,13,7],[14,9,16,5]]
demanda = [40,20,30,30]
oferta = [35,50,40]'''

costos = [[7,3,8,8],[5,5,6,8],[7,4,9,10]]
demanda = [150,150,120,180]
oferta = [100,200,300]

'''costos = [[5,7],[8,5],[6,6]]
demanda = [1200,700]
oferta = [900,500,600]'''
nuevoCostos = []

sumaOferta = 0
sumaDemanda = 0
for i in oferta:
    sumaOferta = sumaOferta + i
for i in demanda:
    sumaDemanda = sumaDemanda + i
    
if(sumaDemanda != sumaOferta):
    print("La tabla no esta equilibrada")
else:
     print("La tabla esta equilibrada")
if(sumaDemanda<sumaOferta):
    demanda.append(sumaOferta-sumaDemanda)
    for i in costos:
        i.append(0)
    costos = np.array(costos)
else:
    oferta.append(sumaDemanda-sumaOferta)
#print(oferta)
#print(demanda)
print(np.array(costos))
n = np.shape(costos)
numero1 = n[0]
numero2 = n[1]
for i in range(numero1):
    t = []
    for j in range(numero2):
        t.append(0)
    nuevoCostos.append(t)

i = 0  
j = 0 
asignados = 0
while (i != numero1 or j != numero2):
    x = 0
    if (oferta[i] < demanda[j]):
        x = oferta[i]
    else:
        x = demanda[j]
    oferta[i] -= x
    demanda[j] -= x
    nuevoCostos[i][j] = x
    asignados += 1
    if (oferta[i] == 0 and i < numero1):
        i += 1
    if (demanda[j] == 0 and j < numero2):
        j += 1

costoTotal = 0
print(np.array(nuevoCostos))
for i in range(numero1):
    for j in range(numero2):
        costoTotal += nuevoCostos[i][j] * costos[i][j] 
if((n[0]+n[1]-1)<=5):
    print("La tabla esta balanceada")
else:
     print("La tabla NO esta balanceada")
print("Costo Total =", costoTotal)
