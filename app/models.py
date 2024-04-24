from .db_connection import Base
from sqlalchemy import Column, Integer, String, Boolean, CheckConstraint

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, autoincrement=True, unique=True, nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(120), nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    level = Column(Integer, default=1, nullable=False)
    parent_id = Column(Integer, nullable=True)
    
    __table_args__ = (
        # CheckConstraint("LENGTH(name) > 0", name = "name_length_check"),
        # CheckConstraint("LENGTH(slug) > 0", name = "slug_length_check"),
        CheckConstraint()
    )