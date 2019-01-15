#利用递归算法写的斐波那契数列，程序简单，效率不高。n>35后几乎无法运算。

def fab(n):
    if n < 1:
        return -1
    
    if (n == 1) or (n == 2):
        return 1

    if n > 2:
        return fab(n-1)+fab(n-2)


n = int(input('输入一个整数：'))
result= fab(n)
if result!=-1:
    print('fab(%d)=%d' % (n,result))
