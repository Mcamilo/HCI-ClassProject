import numpy as np
#x['horas_de_sono','horas_de_estudo']
# x = np.array(([3,5], [5,1], [10,2]), dtype=float)
#y['nota']
# y = np.array(([75], [82], [93]), dtype=float)

#Como os dados possuem diferentes Ranges, notas de 0 a 100 e horas 0 a infinito teoricamente, 
#e necessario a realizacao de uma normalizacao dos dados, ou scaling o que transforma os dados para uma mesma unidade

#x = x/np.amax(x, axis=0) #Limite e o maior valor do eixo 0 (horas_de_sono)
#y = y/100 #Limite e 100
class NeuralNetwork(object):
	"""docstring for NeuralNetwork"""
	def __init__(self, inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons):
		super(NeuralNetwork, self).__init__()
		#define hyperparametros
		# self.inputLayerNeurons = 2
		# self.hiddenLayerNeurons = 3
		# self.outputLayerNeurons = 1

		#sinapses --> matrizes de valores aleatorios que sao multiplicadas por matrizes de valores de neuronios de camadas anteriores
		#Como a Rede a de 2 camadas(nao se conta a camada de saida), havera 2 matrizes de pesos(sinapses que conectam os neuronios)
		
		#2 por 3 -> matriz de pesos que multiplicara a camada de entrada com a camada escondida
		self.W1 = np.random.rand(inputLayerNeurons, hiddenLayerNeurons)
		#3 por 1 -> matriz de pesos que multiplicara a camada escondida com a camada de saida
		self.W2 = np.random.rand(hiddenLayerNeurons, outputLayerNeurons)
	
	#metodo para calcular os valores entre os neuronios e as sinapses
	def feedForward(self, x):
		#z2 -> atividade das sinapses entre a camada de entrada e a camada escondida
		# print("Valores de Entrada: ")
		# print(x)
		# print("Valores de Sinapse da pr")
		self.z2 = np.dot(x, self.W1)	
		#aplicacao de uma funcao de ativacao do resultado obtido da multiplicacao da sinapse anterior
		self.a2 = self.sigmoid(self.z2)
		#z3 -> atividade das sinapses entre a camada escondida e a camada de saida
		self.z3 = np.dot(self.a2, self.W2)
		#resultado final yhat -> representacao de y(nota)
		yHat = self.sigmoid(self.z3)
		return yHat

	def sigmoid(self, z):
		#funcao de ativacao sigmoidal
		return 1/(1+np.exp(-z))

