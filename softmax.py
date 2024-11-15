import numpy as np

inputs = [0,2,2.2,-10,5,10]
exp_values = np.exp(inputs)

print("Input data : ", inputs)
print("exp values: ", exp_values)

norm_values= exp_values/np.sum(exp_values)

print("normalize values : ", norm_values)
print("sum of normalize values : ", sum(norm_values))