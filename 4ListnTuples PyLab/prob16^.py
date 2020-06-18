from itertools import combinations
def sublist(l1):        
    sub=[]
    for i in range(1,len(l1)+1):
        temp=[list(x) for x in combinations(l1,i)]
        if len(temp)>0:
            sub.extend(temp)
    return sub
list1=[1,2,3]
print(sublist(list1))
