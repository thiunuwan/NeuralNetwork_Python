import numpy as np

layer_inputs =[ [0,2,2.2,-10,5,10],
          [1,2,2,-15,8,12],
          [0,2,-2,8,5,6] ]

exp_values = np.exp(layer_inputs)

print("Input data : ", layer_inputs )
print("exp values: ", exp_values)


norm_values= exp_values/np.sum(exp_values, axis=1,keepdims=True)

print("normalize values : ", norm_values)
print("sum of normalize values : ", sum(norm_values))