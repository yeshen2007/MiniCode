#利用迭代法写的斐波那契数列，效率高于递归算法

def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    
    if n < 1:
        print('输入错误！')
        return -1
    
    if (n == 1) or (n == 2):
        return 1
    
    while(n-2)>0:
        n3=n1+n2
        n1=n2
        n2=n3
        n-=1
        
    return n3


n = int(input('输入一个整数：'))
result= fab(n)
if result!=-1:
    print('fab(%d)=%d' % (n,result))
