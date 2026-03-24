# This program calculates the product of two numbers entered by the user.
# Python 中函数定义后，调用的核心格式是：函数名(参数)，分无参函数和有参函数两种情况。
# 情况 1：调用无参函数（函数定义时()内无参数）
# 定义格式：def 函数名(): 函数体
# 调用格式：函数名()
# 情况 2：调用有参函数（函数定义时()内有形参）
# 必须给形参传对应的值，否则会报错，主要有 2 种传参方式：
# ① 位置传参（最常用）
# 按形参定义的顺序，依次传入值
# 函数定义：形参顺序a→b
# def product_of_two_nums(a, b):
    # return a * b
# 位置传参：第一个值给a，第二个给b
# product_of_two_nums(3, 5)  # 结果15
# ② 关键字传参（指定形参名，顺序可乱）
# 直接写形参名=值，不用严格按形参顺序
# product_of_two_nums(b=5, a=3)  # 结果还是15，顺序不影响
# 函数有返回值时，如何接收结果
# 如果函数用return返回了结果，调用时可以用变量接收结果
# 用result变量接收函数的返回值，后续可打印、计算、复用
# result = product_of_two_nums(3,5)
# 如果不需要复用结果，也可以直接调用并打印
# print(product_of_two_nums(3,5))  # 直接输出15

def product_of_two_nums(a, b):
    return a * b

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
result = product_of_two_nums(a, b)
print("The product of the two numbers is:", result)