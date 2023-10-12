# 输入⼀个字符串，判断字符串中是否含有"ol"这个⼦串，若有把所有的"ol"替换为"fzu"，最后把字符串倒序输出
str_1 = input()
str_2 = []
str_replaced = "ol"
if str_replaced in str_1 :
    str_2 = str_1.replace(str_replaced,"fzu")
print(str_2[::-1])
