# 集合推导式
# 语法：{表达式 for 变量 in 可迭代对象 if 条件}
# 特点：自动去重

nums = [1, 2, 2, 3, 3, 3]
s = {x for x in nums}
print(s)  # {1,2,3}

# 带条件
even_set = {x for x in range(10) if x % 2 == 0}
print(even_set)  # {0,2,4,6,8}