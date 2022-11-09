n = int(input())
res=[]
gradelist=[]

for i in range(n):
    name=input()
    grade=float(input())
    res.append([name, grade])
    gradelist.append(grade)
#print(res)
#print(gradelist)

find = sorted(set(gradelist))
low = find[1]
#print(find)
#print(low)

name=[]
for item in res:
    if low==item[1] :
        name.append(item[0])
#print(name)

name.sort()
#print(name)

for z in name:
    print(z)


