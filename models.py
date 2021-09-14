from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm import backref

from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    email = Column(String, unique=True, index=True)
    password = Column(String)



class UserDetail(Base):
    __tablename__ = "user_detail"

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    user = relationship("User", backref=backref("user_detail", uselist=False))

    username = Column(String)
    full_name = Column(String)
    age = Column(Integer)

    groups_id = Column(Integer, ForeignKey("groups.id"), nullable=True)