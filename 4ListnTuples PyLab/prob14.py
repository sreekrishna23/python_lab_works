sam=[1,2,2,3,4,4,4,5,5,6,6]
ans=[]
for i in sam:
    if i not in ans:
        ans.append(i)
print(ans)
