import os
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func, Table
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    name = Column(String(20), nullable=False)
    lastname = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
    date_of_suscription = Column(DateTime, default=func.now())

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    description = Column(String(250))

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    climate = Column(String(50))
    terrain = Column(String(50))

class Favourite(Base):
    __tablename__ = 'favourites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship(User, backref='favorites')
    character = relationship(Character, backref='favorites')
    planet = relationship(Planet, backref='favorites')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')