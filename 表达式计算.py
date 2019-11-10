def solve1(s:str):
    s+='#'
    fuhao=['#']
    jisuan=[]
    for i in range(len(s)):
        if s[i]=='#':
           for k in range(len(fuhao)-1,0,-1):
               jisuan+=[fuhao.pop()]
        if s[i]=='(' or s[i]=='/' or s[i]=='*':
            jisuan+=[s[i]]
        if s[i]==')':
            while(fuhao[len(fuhao)-1]!='('):
                jisuan+=[fuhao.pop()]
            fuhao.pop()
        if s[i]=='+' or s[i]=='-':
            if fuhao[len(fuhao)-1]=='#' or fuhao[len(fuhao)-1]=='(':
                jisuan+=[s[i]]
            else:
                while(fuhao[len(fuhao)-1]!='(' or fuhao[len(fuhao)-1]!='#'):
                    jisuan+=[fuhao.pop()]
                fuhao+=[s[i]]
        else:
            jisuan+=[s[i]]
    
                
    i=0
    while(len(jisuan)>1):
        if jisuan[i]=='*':
           jisuan[i-2]*=jisuan[i-1]
           jisuan.pop(i-1)
           jisuan.pop(i-1)
           i-=1
        if jisuan[i]=='+':
           jisuan[i-2]+=jisuan[i-1]
           jisuan.pop(i-1)
           jisuan.pop(i-1)
           i-=1
        if jisuan[i]=='-' :
            jisuan[i-2]-=jisuan[i-1]
            jisuan.pop(i-1)
            jisuan.pop(i-1)
            i-=1
        if jisuan[i]=='/':
            jisuan[i-2]/=jisuan[i-1]
            jisuan.pop(i-1)
            jisuan.pop(i-1)
            i-=1
    return jisuan[0]

a='1+3*4'
print(solve1(a))
        







