# 定义Item模型，包含id,name,price,description等字段
class Item(Base):
    __tablename__ = "items" # 定义表名

    id = Column(Integer, primary_key=True, index=True) # 定义id字段，主键，自增
    name = Column(String, index=True) # 定义name字段，字符串类型，索引
    price = Column(Float) # 定义price字段，浮点数类型
    description = Column(String) # 定义description字段，字符串类型

# 实现CRUD操作的函数
# 示例：创建一个新商品并保存到数据库
def create_item(db, name: str, price: float, description: str):
    new_item = Item(name=name, price=price, description=description)
    db.add(new_item) # 将新商品添加到数据库会话
    db.commit() # 提交事务，将数据保存到数据库
    db.refresh(new_item) # 刷新实例，获取数据库生成的ID等信息
    return new_item

# 示例：查询商品
def get_item(db, item_id: int):
    return db.query(Item).filter(Item.id == item_id).first() # 根据商品ID查询商品信息

# 示例：更新商品信息
def update_item(db, item_id: int, name: str = None, price: float = None, description: str = None):
    item = db.query(Item).filter(Item.id == item_id).first() # 查询商品
    if item:
        if name:
            item.name = name
        if price:
            item.price = price
        if description:
            item.description = description
        db.commit() # 提交事务，保存更新后的数据
        db.refresh(item) # 刷新实例，获取最新数据
    return item

# 示例：删除商品
def delete_item(db, item_id: int):
    item = db.query(Item).filter(Item.id == item_id).first() # 查询商品
    if item:
        db.delete(item) # 删除商品
        db.commit() # 提交事务，保存删除操作
    return item