import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, ForeignKey('planets.id'), ForeignKey('characters.id'), primary_key=True)
    name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    user_name = Column(String(250), default= {name})
    password = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    age = Column(Integer, nullable=True)


class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, ForeignKey('favs.characters_id'), primary_key=True)
    name = Column(String(250), nullable=False)
    Related_Starships = Column(String(250), nullable=False)
    Related_Vehicles = Column(String(250), nullable=False)
    Related_Films = Column(String(250), nullable=False)
    Homeworld = Column(String(250), nullable=False)

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, ForeignKey('favs.planets_id'), primary_key=True)
    name = Column(String(250), nullable=False)
    Residents = Column(String(250), nullable=False)
    Related_Films = Column(String(250), nullable=False)

class Favs(Base):
    __tablename__ = 'Favs'
    user_id = Column(Integer, primary_key=True)
    planets_id = Column(String(250), ForeignKey('planets.id'), nullable=False)
    characters_id = Column(Integer, ForeignKey('characters.id'))
    total = Column(Integer )
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result= render_er(Base, 'diagram.png')
    print('Success! Check the diagram.png file')

except Exception as e:
    print ('There was a problem generating the diagram')
    raise e
