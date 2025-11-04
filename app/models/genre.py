from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from typing import Optional
from ..db import db

class Genre(db.Model):
    # Column names
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]

    @classmethod
    def from_dict(cls, genre_data):
        
        new_genre = cls(name=genre_data['name'])
        
        return new_genre
    
    def to_dict(self):
        genre_dict = {}
        
        genre_dict['id'] = self.id
        genre_dict['name'] = self.name
        
        return genre_dict
