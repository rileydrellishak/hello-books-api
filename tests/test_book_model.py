import pytest
from app.models.book import Book

def test_from_dict_returns_book(client):
    book_data = {
        'title': 'Harry Potter and the Chamber of Secrets',
        'description': 'Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past.'
    }

    new_book = Book.from_dict(book_data)

    assert new_book.title == book_data['title']
    assert new_book.description == book_data['description']

def test_from_dict_with_no_title():
    # Arrange
    book_data = {
        "description": "Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past."
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'title'):
        new_book = Book.from_dict(book_data)

def test_from_dict_with_no_description():
    # Arrange
    book_data = {
        "title": "Harry Potter and the Chamber of Secrets"
    }

    # Act & Assert
    with pytest.raises(KeyError, match = 'description'):
        new_book = Book.from_dict(book_data)

def test_from_dict_with_extra_keys():
    # Arrange
    book_data = {
        "extra": "some stuff",
        'title': 'Harry Potter and the Chamber of Secrets',
        'description': 'Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past.',
        "another": "last value"
    }

    # Act
    new_book = Book.from_dict(book_data)

    # Assert
    assert new_book.title == book_data['title']
    assert new_book.description == book_data['description']