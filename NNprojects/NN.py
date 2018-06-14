import numpy as np
#x['horas_de_sono','horas_de_estudo']
# x = np.array(([3,5], [5,1], [10,2]), dtype=float)
#y['nota']
# y = np.array(([75], [82], [93]), dtype=float)

#Como os dados possuem diferentes Ranges, notas de 0 a 100 e horas 0 a infinito teoricamente, 
#é necessário a realização de uma normalização dos dados, ou scaling o que transforma os dados para uma mesma unidade

#x = x/np.amax(x, axis=0) #Limite é o maior valor do eixo 0 (horas_de_sono)
#y = y/100 #Limite é 100

class NeuralNetwork(object):
	"""docstring for NeuralNetwork"""
	def __init__(self, inputLayerNeurons, outputLayerNeurons, outputLayerNeurons):
		super(NeuralNetwork, self).__init__()
		#define hyperparâmetros
		self.inputLayerNeurons = 2
		self.hiddenLayerNeurons = 3
		self.outputLayerNeurons = 1

		#sinapses --> matrizes de valores aleatórios que são multiplicadas por matrizes de valores de neuronios de camadas anteriores
		#Como a Rede é de 2 camadas(não se conta a camada de saída), haverá 2 matrizes de pesos(sinapses que conectam os neurônios)
		
		#2 por 3 -> matriz de pesos que multiplicará a camada de entrada com a camada escondida
		self.W1 = np.random.rand(self.inputLayerNeurons, self.hiddenLayerNeurons)
		#3 por 1 -> matriz de pesos que multiplicará a camada escondida com a camada de saida
		self.W2 = np.random.rand(self.hiddenLayerNeurons, self.outputLayerNeurons)
	
	#metodo para calcular os valores entre os neuronios e as sinapses
	def feedForward(self, x):
		#z2 -> atividade das sinapses entre a camada de entrada e a camada escondida
		self.z2 = np.dot(x, self.W1)	
		#aplicação de uma função de ativação do resultado obtido da multiplicação da sinapse anterior
		self.a2 = sigmoid(self.z2)
		#z3 -> atividade das sinapses entre a camada escondida e a camada de saída
		self.z3 = np.dot(self.a2, self.W2)
		
		#resultado final ŷ -> representação de y(nota)
		yHat = sigmoid(self.z3)
		return yHat

	def sigmoid(self, z):
		#funcao de ativacao sigmoidal
		return 1/(1+np.exp(-z))

