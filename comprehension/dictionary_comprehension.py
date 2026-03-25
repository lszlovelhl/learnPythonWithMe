# 语法：{键: 值 for 变量 in 可迭代对象 if 条件}

# 数字 → 平方 的字典
square_dict = {x: x**2 for x in range(5)}
print(square_dict)  # {0:0, 1:1, 2:4, 3:9, 4:16}

# 从列表转字典
words = ['a', 'b', 'c']
word_len = {w: len(w) for w in words}
print(word_len)  # {'a':1, 'b':1, 'c':1}