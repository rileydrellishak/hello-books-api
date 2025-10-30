from sqlalchemy.orm import Mapped, mapped_column
from ..db import db

class Book(db.Model):
    # Column names
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    title: Mapped[str]
    description: Mapped[str]

    @classmethod
    def from_dict(cls, book_data):
        return Book(title=book_data['title'], description=book_data['description'])
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description
            }




# WAVES 1-2 BELOW
# Goal: client sends a request to get all existing books so they can see a list of books with their id, title, and description.

# class Book:
#     def __init__(self, id, title, description):
#         self.id = id
#         self.title = title
#         self.description = description

# books = [
#     Book(1, "Fictional Book", "A fantasy novel set in an imaginary world."),
#     Book(2, "Wheel of Time", "A fantasy novel set in an imaginary world."),
#     Book(3, "Fictional Book Title", "A fantasy novel set in an imaginary world."),
#     Book(4, "Twilight", "A paranormal romance that follows Bella as she navigates a relationship with a vampire, confronts supernatural danger, and learns to deal with the consequences of her decisions."),
#     Book(5, "Harry Potter and the Sorcerer's Stone", "An orphaned boy discovers he is a wizard on his eleventh birthday and enrolls in a magical school, where he and his new friends must prevent a dark wizard from regaining power."),
#     Book(6, "The Hunger Games", "In the dystopian nation of Panem, the protagonist Katniss Everdeen must volunteer as tribute in place of her younger sister to fight to the death in the televised Hunger Games, a televised annual event held as punishment for a past rebellion.")
# ]