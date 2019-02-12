N,A,D=map(int,input().split())
an=A
for i in range(1,N):
 an=an+D
b=A+an
s=N*b//2
print(s)
 
