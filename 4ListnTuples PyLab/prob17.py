from functools import reduce
sum = reduce(lambda x,y: x+y,[k for k in range(1,11)])
print(sum)
