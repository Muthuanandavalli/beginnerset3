N=int(input())
a=list(map(int,input().split()))
y=sorted(a)
for c in range(0,len(y)):
	print(y[c],end=" ")
