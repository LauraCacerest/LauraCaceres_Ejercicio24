import numpy as np
import matplotlib.pyplot as plt



def probabilidad (x,lamb):
    return np.exp(-x/lamb)/(1*(np.exp(-1.0/lamb)-np.exp(-20.0/1))

x=np.array ([1.2,2.5,2.8,5.0])
lamda=np.linspace(0.1,20.0,100.0)
lc=np.ones(1000)
iniciando=0.0

for i in range (0,len(lc)):
    for j in range(0,4):
        lc[i] = lc[i]*probabilidad(x[j],lamb[i])
    iniciando += probabilidad[i]

probabilidad=probabilidad/iniciando
plt.plot(lamb,probabilidad)
plt.title('Decaimiento Radioactivo probabilidad')
plt.xlabel('Lambda')
plt.ylabel ('Probabilidad de lambda')
