sam="how are you"
vow="aeiou "
##ans=[]
##for i in sam :
##    if i not in vow:
##        ans.append(i)
##print(ans)

print([con for con in sam if con not in vow ])
