from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel, Field
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from argon2 import PasswordHasher
from passlib.context import CryptContext

# ______________________ Password Hashing Setup ______________________
# 改用 argon2
pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

# ______________________ Database Setup ______________________
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# ____________________ Database Models ______________________
class Item(Base):
    __tablename__ = "items"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)

# Create the database tables
Base.metadata.create_all(bind=engine)

# ____________________ Pydantic Schemas ______________________
# Pydantic model for item creation
class ItemCreate(BaseModel):
    name: str
    description: str | None = None
    price: float

# Pydantic model for item response
class ItemResponse(BaseModel):
    id: int
    name: str
    description: str | None = None
    price: float

    class Config:
        orm_mode = True # allow ORM objects to be returned as JSON

class UserCreate(BaseModel):
    username: str = Field(min_length=3, max_length=50)
    password: str = Field(min_length=6)

class UserResponse(BaseModel):
    id: int
    username: str

    class Config:
        orm_mode = True

# ______________________ Database Dependency ______________________
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_password_hash(password):
    return pwd_context.hash(password)

# return same format
def resp(code=200, msg="Success", data=None):
    return {"code": code, "msg": msg, "data": data}

# ______________________ FastAPI App ______________________
app = FastAPI(title="Item & User Management System")

# ______________________ API Endpoints ______________________
# __________________________ Item Endpoints __________________________
# Endpoint to create a new item
@app.post("/items/", response_model=ItemResponse)
def create_item(item: ItemCreate, db: SessionLocal = Depends(get_db)):
    db_item = Item(name=item.name, description=item.description, price=item.price)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

# Endpoint to get an item by ID
@app.get("/items/{item_id}", response_model=ItemResponse)
def read_item(item_id: int, db: SessionLocal = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

# Endpoint to get all items
@app.get("/items/", response_model=list[ItemResponse])
def read_items(skip: int = 0, limit: int = 10, db: SessionLocal = Depends(get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items

# Endpoint to update an item
@app.put("/items/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemCreate, db: SessionLocal = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.name = item.name
    db_item.description = item.description
    db_item.price = item.price
    db.commit()
    db.refresh(db_item)
    return db_item

# Endpoint to delete an item
@app.delete("/items/{item_id}", response_model=ItemResponse)
def delete_item(item_id: int, db: SessionLocal = Depends(get_db)):
    db_item = db.query(Item).filter(Item.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return db_item

# __________________________ User Endpoints __________________________
# Endpoint to create a new user
@app.post("/register/")
def register_user(user: UserCreate, db: SessionLocal = Depends(get_db)):
    existsing_user = db.query(User).filter(User.username == user.username).first()
    if existsing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    password = get_password_hash(user.password)
    db_user = User(username=user.username, password=password)
    db.add(db_user)
    db.commit()
    return resp(msg="User registered successfully", data={"username": db_user.username})

# Endpoint to get user details (for demonstration, no authentication implemented)
@app.get("/users/{user_id}", response_model=UserResponse)
def read_user(user_id: int, db: SessionLocal = Depends(get_db)):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user