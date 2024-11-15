import numpy as np


# Model layer of neurons (with numpy)

inputs =[ [1.8,7.5,4.2,5] , [5.8,3.5,4.25,5.6] , [3.8,7.5,4,5] , [1.89,7.35,7.2,9.5] ]

weight_list_lyr1 =[[0.8,1.5,0.2,1.4],[1.8,0.5,4.2,8.4],[0.1,1.2,3.2,0.4]]

weight_list_lyr1 =[[1.8,2.5,3.2,4.4],[2.8,1.5,3.2,1.4],[1.1,1.9,6.2,2.4]]

biases1 = [2,3,-1]
biases2 = [1,4,-2]

# Weights (weight_list) are multiplied by inputs, producing the output for each neuron.
# The biases are added to the result for each corresponding neuron.
layer1_output = np.dot(inputs,np.array(weight_list_lyr1).T) + biases1
layer2_output = np.dot(inputs,np.array(weight_list_lyr1).T) + biases2

print("Output of  the  layer 1 : " ,layer1_output)
print("-----------------------------------------")
print("Output of  the  layer 2: " ,layer2_output)





