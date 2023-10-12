#输入⼀个列表（list），列表中含有字符串和整数，删除其中的字符串元素，然后把剩下的整数升序排序，输出列表
list = ['asd',123,14]
for i in list:
    if isinstance(i,str) :
        list.remove(i)
n = len(list)
for i in range(n-1,-1,-1):
    for j in range(0,i):
        if list[j] > list[j+1] :
            list[j],list[j+1] = list[j+1],list[j]
print(list)