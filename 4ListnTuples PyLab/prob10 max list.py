import functools
mlist=[1,2,33,99,55,63,43]
maxvalue=0
for i in range(1,len(mlist)):
    if mlist[i]>mlist[i-1] :
        if mlist[i]>maxvalue:
            maxvalue=mlist[i]

#print(max(mlist)    )
print("Max Value",maxvalue)

##max=functools.reduce(lambda a,b: a if a>b else b,mlist)
##print("Maximum value is :",max)
