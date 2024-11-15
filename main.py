import numpy as np


# Model layer of neurons (with numpy)

inputs =[1.8,7.5,4.2,5] 

weight_list =[[0.8,1.5,0.2,1.4],[1.8,0.5,4.2,8.4],[0.1,1.2,3.2,0.4]]

biases = [2,3,-1]

output_layer = []

# Weights (weight_list) are multiplied by inputs, producing the output for each neuron.
# The biases are added to the result for each corresponding neuron.
output_layer = np.dot(weight_list,inputs) + biases

print("Output of  the  layer : " ,output_layer)





