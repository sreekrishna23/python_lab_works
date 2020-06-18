mat1=[[1,2,3],[4,5,6],[7,8,9]]
mat2=[[4,2,6],[7,8,3],[5,1,9]]
mat3=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        mat3[i][j]=mat1[i][j]+mat2[i][j]
    if i==0:
        print("Matrix Addition")
    print(mat3[i])
