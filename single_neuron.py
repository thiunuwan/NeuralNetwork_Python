# Model single neuron

inputs =[1.8,7.5,4.2,5] 
weights =[0.8,1.5,0.2,1.4]
bias = 2

output = inputs[0]*weights[0]+ inputs[1]*weights[1]+ inputs[2]*weights[2]+ inputs[3]*weights[3]+bias
print("Output :" ,output)


# Model single neuron with Numpy

import numpy as np
output_np = np.dot(weights,inputs)+bias
print("Output_np :" ,output)