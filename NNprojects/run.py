from nn import NeuralNetwork
import numpy as np
#x['horas_de_sono','horas_de_estudo']
x = np.array(([3,5], [5,1], [10,2]), dtype=float)
#y['nota']
y = np.array(([75], [82], [93]), dtype=float)

#Como os dados possuem diferentes Ranges, notas de 0 a 100 e horas 0 a infinito teoricamente, 
#e necessario a realizacao de uma normalizacao dos dados, ou scaling o que transforma os dados para uma mesma unidade

x = x/np.amax(x, axis=0) #Limite e o maior valor do eixo 0 (horas_de_sono)
y = y/100 #Limite e 100

#class from nn
NN = NeuralNetwork(2,3,1)

#TO-DO dinamizar o metodo feedForward
prediction = NN.feedForward(x)

print("Neural Network: ")
print(prediction)

print("\nCorrect Answer: ")
print(y)
