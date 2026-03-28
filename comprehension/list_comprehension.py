# 列表推导式
# 语法：[表达式 for 变量 in 可迭代对象 if 条件]

# 生成 0~9 的平方列表
squares = [x**2 for x in range(10)]
print(squares)  # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

# 带条件：只保留偶数的平方
even_squares = [x**2 for x in range(10) if x % 2 == 0]
print(even_squares)  # [0, 4, 16, 36, 64]

# 从字符串中提取大写字母
s = "Hello World!"
uppercase_letters = [char for char in s if char.isupper()]
print(uppercase_letters)  # ['H', 'W']

# 生成1-100的偶数列表
even_numbers = [x for x in range(1, 101) if x % 2 == 0]
print(even_numbers)  # [2, 4, 6, ..., 100]