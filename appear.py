d={}
l=[]
a=int(raw_input())
for i in range(0,a):
    l.append(int(raw_input()))
for i in l:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
for i in d:
    if d[i]==1:
        print i
        break