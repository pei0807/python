import numpy as np

array = np.random.randint(30,size=20)
a = [15,13,14,3,8,5,27,17,7,20,6,1,4,11]
print(len(a))
final=0
loop = 0
for j in range(0,len(a)-1,1):
    for i in range(0,len(a)-1-j,1):
        if a[i]>a[i+1]:
            swap = a[i+1]
            a[i+1] = a[i]
            a[i]= swap
        loop = loop+1

print(a)
# print(loop)

#binary search
target = 27
start = round(len(a) / 2)

while 1:
    if a[start]>target:
        prev = start
        start = start -1
        print(prev)
        print(start)
    else:
        prev = start
        start = start+1

    if start<end:
        print(a[start])
        print('index %i' %start)
        break

    else:
        print('not found')

