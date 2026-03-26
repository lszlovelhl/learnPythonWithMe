from fastapi import FastAPI
from pydantic import BaseModel

# 创建 FastAPI 应用
app = FastAPI()

# FastAPI 使用 Pydantic 模型来定义请求体的数据结构,并做数据验证和序列化
class User(BaseModel):
    name: str
    age: int
    city: str | None = None # 可选字段，默认None

# 创建用户接口
@app.post("/user") # POST请求+请求体
def create_user(user: User):
    return {"message": "User created successfully", "user": user}

# 定义用户响应模型（只返回部分字段）
class UserResponse(BaseModel):
    name: str
    age: int
    city: str | None = None

# 指定响应模型，FastAPI 会自动将返回的数据转换为指定的模型格式
@app.get("/user/{user_id}", response_model=UserResponse)
def get_user(user_id: int):
    # 模拟从数据库获取用户数据
    user_data = {"name": "Alice", "age": 30, "city": "New York", "password": "123456"}
    return user_data # 只会返回name、age和city字段，password字段会被自动过滤掉

# 路径参数+查询参数+请求体参数混合使用
@app.put("/user/{user_id}")
def update_user(user_id: int, user: User, is_active: bool = True):
    return {
        "user_id": user_id, # 路径参数
        "update_data": user, # 请求体参数（JSON）
        "is_active": is_active # 查询参数（URL参数）可选，默认值为True
    }

# 练习
# 定义Item模型，包含name: str, price: float, description: str | None = None
class Item(BaseModel):
    name: str
    price: float
    description: str | None = None

# 创建商品接口
@app.post("/items")
def create_item(item: Item):
    return {"message": "Item created successfully", "item": item}

# 获取商品接口，路径参数item_id，查询参数include_description: bool = False
@app.get("/items/{item_id}")
def get_item(item_id: int, include_description: bool = False):
    item_data = {"name": "Sample Item", "price": 9.99, "description": "This is a sample item."}
    if not include_description:
        item_data.pop("description") # 如果不需要描述信息，则从返回数据中移除description字段
    return {"item_id": item_id, "item": item_data}

# 更新商品接口，路径参数item_id，请求体参数Item
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"message": "Item updated successfully", "item_id": item_id, "updated_item": item}

# 根路径接口
@app.get("/")
def home():
    return {"message": "Hello, FastAPI!"}

# 测试接口
@app.get("/test")
def test():
    return{"status": "success", "data": "This is a test endpoint."}

# 路径参数
@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "name": "test item"}

# 查询参数
@app.get("/items")
def get_items(page: int = 1, size: int = 10):
    return {"page": page, "size": size, "items": ["item1", "item2", "item3"]}

# 测试接口
@app.get("/hello/{name}")
def say_hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add")
def add_numbers(a: int, b: int):
    return {"result": a + b}