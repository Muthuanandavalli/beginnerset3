N=int(input())
a=list(map(int,input().split()))
x=sorted(a)
for c in range(0,len(x)):
	if c<(len(x)-1):
		print(x[c],end=" ")
	else:
		print(x[c])
