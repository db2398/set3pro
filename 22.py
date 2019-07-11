daf=int(input())
bar=list(map(int,input().split()))[:daf]
z=sum(bar[0:daf:2])
talk=sum(bar[1:daf:2])
if z>talk:
  print(z)
else:
  print(talk)
