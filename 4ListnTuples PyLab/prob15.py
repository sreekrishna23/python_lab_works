sam=['aba','cat','mam','ab','r','samas']

count=0
for word in sam:
    if len(word)>=2 and word[0]==word[-1]:
        count+= 1
print("no of such words is :",count)

    
        
