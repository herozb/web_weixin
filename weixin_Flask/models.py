
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, UniqueConstraint, Index

Base = declarative_base()

class webuser(Base):
    __tablename__ = 'webuser'

    username = Column(String(15), primary_key=True)
    password = Column(String(15), unique=True)

    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'),
        # Index('ix_id_name', 'name', 'email'),
    )


class userinfos(Base):
    __tablename__ = 'userinfos'

    id = Column(Integer, primary_key=True)
    phone = Column(String(15), index=True, nullable=False)
    staffId = Column(String(10), unique=True)
    pwd = Column(String(6), unique=True)


    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'),
        # Index('ix_id_name', 'name', 'email'),
    )


class taxinfos(Base):
    __tablename__ = 'taxinfos'
    id = Column(Integer, primary_key=True)
    companyName = Column(String(50),unique=True)
    taxNumber = Column(String(18), unique=True)
    address = Column(String(100), unique=True)
    phone = Column(String(15), unique=True)
    bank = Column(String(100), unique=True)
    cardNo = Column(String(25), unique=True)

    __table_args__ = (
        # UniqueConstraint('id', 'name', name='uix_id_name'),
        # Index('ix_id_name', 'name', 'email'),
    )
