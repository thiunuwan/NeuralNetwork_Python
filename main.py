# Model single neuron

inputs =[1.8,7.5,4.2,5] 
weights =[0.8,1.5,0.2,1.4]
bias = 2

output = inputs[0]*weights[0]+ inputs[1]*weights[1]+ inputs[2]*weights[2]+ inputs[3]*weights[3]+bias
print("Output :" ,output)


# Model layer of neurons

inputs =[1.8,7.5,4.2,5] 
weights1 =[0.8,1.5,0.2,1.4]
weights2 =[1.8,0.5,4.2,8.4]
weights3 =[0.1,1.2,3.2,0.4]
bias1 = 2
bias2 = 3
bias3 = -1

output_lyr = [inputs[0]*weights1[0]+ inputs[1]*weights1[1]+ inputs[2]*weights1[2]+ inputs[3]*weights1[3]+bias1 ,
          inputs[0]*weights2[0]+ inputs[1]*weights2[1]+ inputs[2]*weights2[2]+ inputs[3]*weights2[3]+bias2 ,
          inputs[0]*weights3[0]+ inputs[1]*weights3[1]+ inputs[2]*weights3[2]+ inputs[3]*weights3[3]+bias3 ]

print("Output of  the  layer : " ,output_lyr)





