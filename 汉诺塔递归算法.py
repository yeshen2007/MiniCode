#汉诺塔递归算法

def hanoi(n,x,y,z):
    if n < 1:
        return -1
    
    if n == 1:
        print(x,'-->',z)
    else:
        
        #将n-1层从X移动到Y轴上
        hanoi(n-1,x,z,y)
        #将底部最后一层从X轴移动到Z轴上
        print(x,'-->',z)
        #将n-1层从Y轴移动到Z轴上
        hanoi(n-1,y,x,z)
        

n = int(input('输入汉诺塔层数：'))
result = hanoi(n,'X','Y','Z')
if result == -1:
    print('输入的层数有错误！')
        
