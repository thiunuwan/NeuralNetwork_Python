import math

inputs = [0,2,2.2,-10,5,10]
exp_values = []

E=math.e

for i in inputs:
    exp_values.append(E**i)

print("Input data : ", inputs)
print("exp values: ", exp_values)

# calculate the sum of exp values
norm_base =  sum(exp_values)

norm_values= []

for val in exp_values:
    norm_values.append(val/norm_base)

print("normalize values : ", norm_values)
print("sum of normalize values : ", sum(norm_values))