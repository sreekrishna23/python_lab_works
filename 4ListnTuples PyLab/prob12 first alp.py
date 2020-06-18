alp=input("enter an alphabet: ")
sam=['bat','ball','dog','manga','thenga','biryani','dosai','ghee rost']
ans=[]
for i in range(len(sam)):
    if alp==sam[i][0]:
        ans.append(sam[i])
print(ans)
    
##print([sam[i] for i in range(len(sam)) if alp==sam[i][0]])                   
               
