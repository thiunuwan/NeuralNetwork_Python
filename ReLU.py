inputs = [0,2,-1,3.3,-2.7,1.1,2.2,-100,-0.154]
output = []

for i in inputs:
    if i>0:
        output.append(i)
    if i<=0:
        output.append(0)

# for i in inputs:
#   output.append(max(0,i))

print("Input data : ", inputs)
print("Output data : ", output)