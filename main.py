import numpy as np

# Model layer of neurons (with numpy)

X =[ [1.8,7.5,4.2,5] , [5.8,3.5,4.25,5.6] , [3.8,7.5,4,5] , [1.89,7.35,7.2,9.5] ]

class Layer_Dense:
    def __init__(self,n_inputs,n_neurons): 
        self.weights=  0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases

layer1 = Layer_Dense(4,5)
layer2 = Layer_Dense(5,2)

layer1.forward(X)
print("Output of  the  layer 1 : " ,layer1.output)

layer2.forward(layer1.output)
print("Output of  the  layer 2 : " ,layer2.output)





