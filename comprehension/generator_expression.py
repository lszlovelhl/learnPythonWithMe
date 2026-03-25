# 生成器
# 语法：(表达式 for 变量 in 可迭代对象 if 条件)
# 特点：不占内存，一次生成一个值
gen = (x**2 for x in range(10))

print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# 也可以直接转列表
print(list(gen))  # [9, 16, 25, 36, 49, 64, 81]