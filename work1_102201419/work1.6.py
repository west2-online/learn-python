# 创建一个函数，这个函数可以统计一个只有数字的列表中各个数字出现的次数，通过字典方式返回
a = [1,2,1,1,2,3,1,2,1,3,2]
def count_number(a) :
    total = {}
    bool1 = 0
    for i in a :
        for j in total:
            if i == j:
                bool1 = 1
        if bool1 == 1:
            total[i] += 1
        else:
            total[i] = 1
        bool1 = 0
    return total
need_dict = count_number(a)
print(need_dict)