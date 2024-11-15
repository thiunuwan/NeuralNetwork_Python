# Model single neuron

inputs =[1.8,7.5,4.2,5] 
weights =[0.8,1.5,0.2,1.4]
bias = 2

output = inputs[0]*weights[0]+ inputs[1]*weights[1]+ inputs[2]*weights[2]+ inputs[3]*weights[3]+bias
print("Output :" ,output)


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





