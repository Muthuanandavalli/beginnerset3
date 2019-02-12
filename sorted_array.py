N=int(input())
a=list(map(int,input().split()))
y=sorted(a)
for c in range(0,len(y)):
	if c<(len(y)-1):
		print(y[c],end=" ")
	else:
		print(y[c])
