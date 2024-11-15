import numpy as np

# Model layer of neurons (with numpy)

# Set the seed
np.random.seed(0)

# sample input data
def create_data(samples, classes):
    X = np.zeros((samples*classes, 2))
    y = np.zeros(samples*classes, dtype='uint8')
    for class_number in range(classes):
        ix = range(samples*class_number, samples*(class_number+1))
        r = np.linspace(0.0, 1, samples)
        t = np.linspace(class_number*4, (class_number+1)*4, samples) + np.random.randn(samples)*0.2
        X[ix] = np.c_[r*np.sin(t*2.5), r*np.cos(t*2.5)]
        y[ix] = class_number
    return X, y


class Layer_Dense:
    def __init__(self,n_inputs,n_neurons): 
        self.weights=  0.10 * np.random.randn(n_inputs,n_neurons)
        self.biases = np.zeros((1,n_neurons))
    def forward(self,inputs):
        self.output = np.dot(inputs,self.weights) + self.biases


class Activation_ReLU:
    def forward(self,inputs):
        self.output=np.maximum(0,inputs)


X,y =create_data(100,3)

layer1 = Layer_Dense(2,5)

layer1.forward(X)
print("Output (u) of  the  layer 1 before  activation func : " ,layer1.output)

print("------------------------------------------------------------------")

activation1 = Activation_ReLU()
activation1.forward(layer1.output)
print("Output (y) of  the  layer 1 after  activation func : " ,activation1.output)





