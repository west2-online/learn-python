"""设计⼀个商品类，它具有的私有数据成员是商品序号、商品名、单价、总数量和剩余数量。具有的 公有成员函数是：初始化商品信息的构造函数__init__，
显示商品信息的函数display，计算已售出 商品价值income，修改商品信息的函数setdata"""

class Commodity:
    def __init__(self,id,name,price,sum,remain):
        self.__product_id = id
        self.__product_name = name
        self.__product_price = price
        self.__product_sum = sum
        self.__product_remain = remain

    def display(self):
        print("id = %s\nname = %s\nprice = %s\nsum = %s\nremain = %s" %(self.__product_id,self.__product_name,self.__product_price,self.__product_sum,self.__product_remain))

    def income(self):
        price =self.__product_price
        sum = self.__product_sum
        remain = self.__product_remain
        return price*(sum-remain)

    def setdata(self,id,name,price,sum,remain):
        self.__product_id = id
        self.__product_name = name
        self.__product_price = price
        self.__product_sum = sum
        self.__product_remain = remain

cookie = Commodity(10001,'cookie',12,200,100)
cookie.display()
ke = cookie.income()
print(ke)
