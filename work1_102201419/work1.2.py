# 输出九九乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print('%d*%d=%d'%(j,i,j*i),end='\t')
    print("\n")