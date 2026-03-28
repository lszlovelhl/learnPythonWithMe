# 常见数据库类型对比
# 关系型数据库SQL：MySQL、PostgreSQL、Oracle、SQL Server等
    # 特点：结构化数据、支持复杂查询、事务处理、数据一致性
    # 适用场景：金融、电子商务、企业应用等需要强数据一致性的场景
# 非关系型数据库NoSQL：MongoDB、Cassandra、Redis等
    # 特点：非结构化数据、灵活的数据模型、高性能、可扩展性
    # 适用场景：大数据、实时分析、社交媒体、物联网等需要高性能和灵活数据模型的场景
# 内存数据库：Redis、Memcached等
    # 特点：数据存储在内存中，极快的读写速度，适合缓存和实时数据处理
    # 适用场景：缓存、会话管理、实时分析等需要快速访问数据的场景

from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 创建数据库引擎，连接到SQLite数据库
SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False} # SQLite特有的参数，允许多线程访问数据库
)

# 创建会话，用于与数据库进行交互
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 定义基类，用于创建数据库模型
Base = declarative_base()

# 定义User模型，继承自Base
class User(Base):
    __tablename__ = "users" # 指定数据库表名

    id = Column(Integer, primary_key=True, index=True) # 主键，自动递增
    name = Column(String, index=True) # 用户名，索引
    age = Column(Integer) # 年龄
    city = Column(String) # 城市
    salary = Column(Float) # 薪水
    email = Column(String, unique=True, index=True) # 邮箱，唯一索引

# 创建数据库表
Base.metadata.create_all(bind=engine)

# 创建一个新的数据库会话
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() # 关闭数据库会话，释放资源

# 示例：创建一个新用户并保存到数据库
def create_user(db, name: str, age: int, city: str, salary: float, email: str):
    new_user = User(name=name, age=age, city=city, salary=salary, email=email)
    db.add(new_user) # 将新用户添加到数据库会话
    db.commit() # 提交事务，将数据保存到数据库
    db.refresh(new_user) # 刷新实例，获取数据库生成的ID等信息
    return new_user

# 示例：查询用户
def get_user(db, user_id: int):
    return db.query(User).filter(User.id == user_id).first() # 根据用户ID查询用户信息

# 示例：更新用户信息
def update_user(db, user_id: int, name: str = None, age: int = None, city: str = None, salary: float = None, email: str = None):
    user = db.query(User).filter(User.id == user_id).first() # 查询用户
    if user:
        if name:
            user.name = name
        if age:
            user.age = age
        if city:
            user.city = city
        if salary:
            user.salary = salary
        if email:
            user.email = email
        db.commit() # 提交事务，保存更新后的数据
        db.refresh(user) # 刷新实例，获取最新数据
    return user

# 示例：删除用户
def delete_user(db, user_id: int):
    user = db.query(User).filter(User.id == user_id).first() # 查询用户
    if user:
        db.delete(user) # 删除用户
        db.commit() # 提交事务，保存删除操作
    return user

# 示例：查询所有用户
def get_all_users(db):
    return db.query(User).all() # 查询所有用户信息

# 示例：根据城市查询用户
def get_users_by_city(db, city: str):
    return db.query(User).filter(User.city == city).all() # 根据城市查询用户信息

# 示例：根据年龄范围查询用户
def get_users_by_age_range(db, min_age: int, max_age: int):
    return db.query(User).filter(User.age >= min_age, User.age <= max_age).all() # 根据年龄范围查询用户信息

# 示例：根据薪水范围查询用户
def get_users_by_salary_range(db, min_salary: float, max_salary: float):
    return db.query(User).filter(User.salary >= min_salary, User.salary <= max_salary).all() # 根据薪水范围查询用户信息

# 示例：根据邮箱查询用户
def get_user_by_email(db, email: str):
    return db.query(User).filter(User.email == email).first() # 根据邮箱查询用户信息

# 示例：统计用户数量
def count_users(db):
    return db.query(User).count() # 统计用户数量

# 示例：统计每个城市的用户数量
def count_users_by_city(db):
    return db.query(User.city, func.count(User.id)).group_by(User.city).all() # 统计每个城市的用户数量

# 示例：统计每个年龄段的用户数量
def count_users_by_age_range(db):
    return db.query(func.case([(User.age < 18, '0-17'), (User.age < 30, '18-29'), (User.age < 50, '30-49')], else_='50+'), func.count(User.id)).group_by(func.case([(User.age < 18, '0-17'), (User.age < 30, '18-29'), (User.age < 50, '30-49')], else_='50+')).all() # 统计每个年龄段的用户数量

# 示例：统计每个薪水范围的用户数量
def count_users_by_salary_range(db):
    return db.query(func.case([(User.salary < 30000, '0-29k'), (User.salary < 60000, '30-59k'), (User.salary < 100000, '60-99k')], else_='100k+'), func.count(User.id)).group_by(func.case([(User.salary < 30000, '0-29k'), (User.salary < 60000, '30-59k'), (User.salary < 100000, '60-99k')], else_='100k+')).all() # 统计每个薪水范围的用户数量

# 示例：统计每个城市的平均薪水
def average_salary_by_city(db):
    return db.query(User.city, func.avg(User.salary)).group_by(User.city).all() # 统计每个城市的平均薪水

# 示例：统计每个年龄段的平均薪水
def average_salary_by_age_range(db):
    return db.query(func.case([(User.age < 18, '0-17'), (User.age < 30, '18-29'), (User.age < 50, '30-49')], else_='50+'), func.avg(User.salary)).group_by(func.case([(User.age < 18, '0-17'), (User.age < 30, '18-29'), (User.age < 50, '30-49')], else_='50+')).all() # 统计每个年龄段的平均薪水

# 示例：统计每个薪水范围的平均年龄
def average_age_by_salary_range(db):
    return db.query(func.case([(User.salary < 30000, '0-29k'), (User.salary < 60000, '30-59k'), (User.salary < 100000, '60-99k')], else_='100k+'), func.avg(User.age)).group_by(func.case([(User.salary < 30000, '0-29k'), (User.salary < 60000, '30-59k'), (User.salary < 100000, '60-99k')], else_='100k+')).all() # 统计每个薪水范围的平均年龄

# 测试
if __name__ == "__main__":
    db = next(get_db()) # 获取数据库会话
    # 创建新用户
    user = create_user(db, name="Alice", age=30, city="New York", salary=70000, email="alice@example.com")
    print(f"Created user: {user}", user.id, user.name, user.age, user.city, user.salary, user.email)
    # 查询用户
    user = get_user(db, user_id=1)
    print(f"Queried user: {user}", user.id, user.name, user.age, user.city, user.salary, user.email)
    # 更新用户信息
    updated_user = update_user(db, user_id=1, name="Alice Smith", age=31)
    print(f"Updated user: {updated_user}", updated_user.id, updated_user.name, updated_user.age, updated_user.city, updated_user.salary, updated_user.email)
    # 删除用户
    deleted_user = delete_user(db, user_id=1)
    print(f"Deleted user: {deleted_user}", deleted_user.id, deleted_user.name, deleted_user.age, deleted_user.city, deleted_user.salary, deleted_user.email)
    # 查询所有用户
    users = get_all_users(db)
    print(f"All users: {users}")
    # 根据城市查询用户
    users_in_city = get_users_by_city(db, city="New York")
    print(f"Users in New York: {users_in_city}")
    # 根据年龄范围查询用户
    users_in_age_range = get_users_by_age_range(db, min_age=20, max_age=40)
    print(f"Users aged 20-40: {users_in_age_range}")
    # 根据薪水范围查询用户
    users_in_salary_range = get_users_by_salary_range(db, min_salary=50000, max_salary=100000)
    print(f"Users with salary 50k-100k: {users_in_salary_range}")
    # 根据邮箱查询用户
    user_by_email = get_user_by_email(db, email="alice@example.com")
    print(f"User with email alice@example.com: {user_by_email}")
    # 统计用户数量
    user_count = count_users(db)
    print(f"Total users: {user_count}")
    