#输入三个整数x,y,z，请尝试用多种方式把这三个数由大到小输出
num = []
for i in range(3) :  #选择排序
    word = input()
    num.append(word)

for i in range(2):
    min = i
    for j in range (i+1, 3) :
        if num[j] < num[min] :
            min = j
    num[i], num[min] = num[min], num[i]
print(num)

#print(sorted(num))  内置工具

""" 冒泡排序
for i in range(2,-1,-1):
    for j in range(0,i):
        if num[j] > num[j+1] :
            num[j],num[j+1] = num[j+1],num[j]
    print(num)

print(num)"""