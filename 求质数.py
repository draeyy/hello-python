def isp(x,ip):
    op=True
    for i in ip:
        if x%i==0:
            op=False
        else:
            pass
    return op
def main():
    n=input('退出请按q或Q,n(>2)=')
    while n!='q'and n!='Q':
        n=int(n)
        zs=[2]
        for i in range(3,n+1):
            if isp(i,zs):
                zs.append(i)
            else:
                pass
        k=len(zs)//7
        kp=len(zs)%7
        for i in range(k):
            for j in range(7*i,7*i+7):
                print(zs[j],end=',')
            print('\n')
        for i in range(7*k,len(zs)):
            print(zs[i],end=',')
        n = input('退出请按q或Q,n(>2)=')
main()