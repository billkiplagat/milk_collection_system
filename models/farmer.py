import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
import hashlib


class Farmer(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = 'farmer'
        name = Column(String(100), nullable=False)
        contact_number = Column(String(15), nullable=False, unique=True)
        address = Column(String(255), nullable=False)
        password = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes farmer"""
        if 'password' in kwargs:
            kwargs['password'] = hashlib.md5(kwargs['password']
                                             .encode()).hexdigest()
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Farmer {self.name}>"
