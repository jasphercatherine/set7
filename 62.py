j=int(input())
j=str(j)
f=0
for i in range(0,len(j)):
 if(j[i]=='0' or j[i]=='1'):
  f=1
 else:
  f=0
  break
if(f==1):
 print('yes')
else:
 print('no')
