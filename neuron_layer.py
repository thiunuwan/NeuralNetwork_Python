# Model layer of neurons

inputs =[1.8,7.5,4.2,5] 

weight_list =[[0.8,1.5,0.2,1.4],[1.8,0.5,4.2,8.4],[0.1,1.2,3.2,0.4]]

biases = [2,3,-1]

output_layer = []

for neuron_weights,neuron_bias in zip (weight_list,biases):
    neuron_output=0
    for n_input,n_weight in zip (inputs,neuron_weights):
        neuron_output= neuron_output + (n_input*n_weight)
    neuron_output = neuron_output +  neuron_bias
    output_layer.append(neuron_output)

print("Output of  the  layer : " ,output_layer)





# Model layer of neurons with Numpy

import numpy as np

output_layer_np = []

for neuron_weights,neuron_bias in zip (weight_list,biases):
    neuron_output_np= np.dot(inputs,neuron_weights)
    neuron_output_np= neuron_output_np+  neuron_bias
    output_layer_np.append(neuron_output_np)

print("Output_of _the_layer_np :" ,output_layer_np)