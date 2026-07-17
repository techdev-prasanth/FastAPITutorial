from sqlalchemy import Integer, String, Column , Float , Boolean
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(100), unique=True, index=True, nullable=False)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password = Column(String(255), nullable=False)
    full_name = Column(String(100), nullable=True)
    phone = Column(String(15), nullable=True)
    is_active = Column(Boolean, default=True)