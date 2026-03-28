from pymongo import MongoClient

# 连接本地MongoDB
client = MongoClient("mongodb://localhost:27017/")

# 创建/切换数据库
db = client["mydb"]

# 创建/切换集合（相当于表）
items_col = db["items"]

# 1. 插入一条
item = {"name": "笔记本", "price": 3999, "desc": "游戏本"}
result = items_col.insert_one(item)
print("插入ID:", result.inserted_id)

# 2. 查询所有
for item in items_col.find():
    print(item)

# 3. 条件查询
item = items_col.find_one({"name": "笔记本"})
print("查询到:", item)

# 4. 更新
items_col.update_one({"name": "笔记本"}, {"$set": {"price": 4299}})

# 5. 删除
items_col.delete_one({"name": "笔记本"})