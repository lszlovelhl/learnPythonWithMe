# 文本文件读写
try:
    with open("example.txt", "a+", encoding="utf-8") as file: # "a+" 模式：如果文件不存在则创建，存在则在末尾追加内容，并且可以读取
        file.seek(0)
        content = file.read()
        print(content)
except FileNotFoundError:
    print("文件路径不存在，无法创建")
except PermissionError:
    print("没有文件读写权限")
except Exception as e:
    print(f"文件操作失败：{e}")

with open("example.txt", "a", encoding="utf-8") as file: # "a" 模式：如果文件不存在则创建，存在则在末尾追加内容
    file.write("这是新添加的一行文本。\n")

with open("example.txt", "r+", encoding="utf-8") as file: # "r+" 模式：读写模式，文件必须存在
    content = file.read()
    print(content)

with open("example.txt", "r", encoding="utf-8") as file: # "r" 模式：只读模式，文件必须存在
    content = file.read()
    print(content)

with open("example.txt", "w+", encoding="utf-8") as file: # "w+" 模式：写入模式，如果文件不存在则创建，存在则覆盖原内容
    file.write("这是覆盖原内容的新文本。\n")

with open("example.txt", "w", encoding="utf-8") as file: # "w" 模式：写入模式，如果文件不存在则创建，存在则覆盖原内容
    file.write("这是覆盖原内容的新文本。\n")