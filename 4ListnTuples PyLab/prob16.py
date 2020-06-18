sam=[1,2,3,4]
ans=[]
for i in range(len(sam)+1):
        for j in range(i+1,len(sam)+1):
                f=sam[i:j]
                ans.append(f)
print(ans)
