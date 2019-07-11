ddd1=int(input())
ddd2=list(map(int,input().split()))
ans=int(ddd1/2)
e1=ddd2[:ans]
e2=ddd2[ans::]
if ((sum(e1)//len(e1))==(sum(e2)//len(e2))):
    print("yes")
else:
    print("no")
