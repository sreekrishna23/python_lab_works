import functools
mlist=[1,2,3,4,5,6,7,8,9,10]

#summ=functools.reduce(lambda a,b:a+b,mlist)

summ=0
for item in mlist:
    summ=summ+item

print("Sum is : " +str(summ))
mean=summ/len(mlist)
print("Mean is "+str(mean))
