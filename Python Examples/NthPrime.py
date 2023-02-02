n=int(input())
p=2
b=0
l=[]
while(b<n):
    c=0
    for i in range(1,p+1):
        if(p%i==0):
            c+=1
    if(c==2):
        l.append(p)
        b+=1
    p=p+1
print(l)
print(l[n-1])