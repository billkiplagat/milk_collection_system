#!/usr/bin/python3
import models
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
import hashlib


class Admin(BaseModel, Base):
    if models.storage_t == "db":
        __tablename__ = 'admin'
        username = Column(String(50), unique=True, nullable=False)
        password = Column(String(255), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes admin"""
        if 'password' in kwargs:
            kwargs['password'] = hashlib.md5(kwargs['password']
                                             .encode()).hexdigest()
        super().__init__(*args, **kwargs)

    def __repr__(self):
        return f"<Admin {self.username}>"
