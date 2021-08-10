#KMP algorithm
#prints the no. of times a pattern exists on a string
s="ababcabcabababd"
p="ababd"
cnt=0
pn=len(p)
sn=len(s)
pt=[0]*pn
l=0
pt[0]=0
for i in range(1,pn):
    if p[i]==p[l]:
        l+=1
        pt[i]=l
    else:
        if l!=0:
            l=pt[l-1]
        else:
            pt[i]=0
print(pt)

j=0
for i in range(sn):
    if s[i]==p[j]:
        i+=1
        j+=1
    else:
        j=pt[j-1]
        j=j+1
    if j==pn:
        cnt+=1
        print(str(i-j))
        j=pt[j-1]
print(cnt)
