# 创建一个字典（dict），为字典添加几个键为学号，值为姓名元素，删除学号尾号为偶数的元素，输出字典

student = {1000010:'xiaoming',1000011:'xiaowang',1000012:'xiaozhang',1000015:'xiaochen'}

xuehao = []
for key,value in student.items() :
    if key % 2 == 0 :
        xuehao.append(key)
for key in xuehao :
    del student[key]
print(student)