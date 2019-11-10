block=[]
for i in range(10):
    block+=[(0,i),(i,0),(9,i),(i,9)]
block+=[(1,3),(1,7),(2,3),(2,7),(3,5),(3,6),(4,2),(4,3),(4,4),(5,4),(6,2),(6,6),(7,2),(7,3),(7,4),(7,6),(7,7),(8,1)]
class step:
    def __init__(self,row,column,direction=1):
        self.r=row
        self.c=column
        self.d=direction

def sovle1(block):
    x=step(1,1)
    steps=[x]
    block+=[(x.r,x.c)]
    while(1):
        if x.d==1:
            if (step(x.r,x.c+1).r,step(x.r,x.c+1).c) not in block:
                x=step(x.r,x.c+1)
                steps+=[x]
                block+=[(x.r,x.c)]
                if steps[len(steps)-1].r==8 and steps[len(steps)-1].c==2:
                    return steps
            else:
                x.d+=1
        if x.d==2:
            if (step(x.r+1,x.c).r,step(x.r+1,x.c).c) not in block:
                x=step(x.r+1,x.c)
                steps+=[x]
                block+=[(x.r,x.c)]
                if steps[len(steps)-1].r==8 and steps[len(steps)-1].c==2:
                    return steps
            else:
                x.d+=1
        if x.d==3:
            if (step(x.r,x.c-1).r,step(x.r,x.c-1).c) not in block:
                x=step(x.r,x.c-1)
                steps+=[x]
                block+=[(x.r,x.c)]
                if steps[len(steps)-1].r==8 and steps[len(steps)-1].c==2:
                    return steps
            else:
                x.d+=1
        if x.d==4:
            if (step(x.r-1,x.c).r,step(x.r-1,x.c).c) not in block:
                x=step(x.r-1,x.c)
                steps+=[x]
                block+=[(x.r,x.c)]
                if steps[len(steps)-1].r==8 and steps[len(steps)-1].c==2:
                    return steps
            else:
                steps.pop()
                block+=[(x.r,x.c)]
                x=steps[len(steps)-1]
result=sovle1(block)
qq=[]
for i in range(len(result)):
    qq+=[(result[i].r,result[i].c)]
print(qq)





