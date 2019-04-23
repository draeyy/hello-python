from math import*
def main():
    def f(i):
        x = i
        fi = eval(fx)
        return fi
    fx=input('请输入f(x),退出请按q')
    while fx!='q':
        a=float(input('区间左端点'))
        b=float(input('区间右端点'))
        e=float(input('请输入精确度'))
        if f(a)*f(b)<0:
            while b - a > e:
                c = (a + b) / 2
                if f(a) * f(c) < 0:
                    b = c
                elif f(b) * f(c) < 0:
                    a = c
                else:
                    break
            print(c)
        else:
            print('a与b之间无法用二分法求根')
        fx = input('请输入f(x),退出请按q')
    print('程序已退出')
main()



