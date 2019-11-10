x=[i for i in range(25)]
y=[]
z=[]
def hanoi(a:list,b:list,c:list):
    if len(a)==1:
        c.insert(0,a.pop())
    else:
        a1,c,b=hanoi(a[0:len(a)-1],c,b)
        a=[a[len(a)-1]]
        c.insert(0,a.pop())
        t=c.pop()#注意hanoi每一次要和n的形式完全一样
        b,a,c=hanoi(b,a,c)
        c.append(t)
    return a,b,c
x,y,z=hanoi(x,y,z)
print(x)
print(y)
print(z)

