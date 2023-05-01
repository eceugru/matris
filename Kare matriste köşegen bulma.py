n=int(input("satır :"))
c=0
M=[[0 for i in range(n)] for x in range(n)]
print(M)
for i in range(n):
    for j in range(n):
        M[i][j]=int(input("m :"))
print(M)
for i in range(n):
    for j in range(i,i+1):
        top=M[0][0]
        if top==M[i][j]:
            print(M[i][j])
            c+=1
if c==n:
    print("True")
else:
    print("False")


