n=int(input())
if n%10!=0:
	x=n%10
	n=n+(10-x)
	print(n)
else:
	print(n)
