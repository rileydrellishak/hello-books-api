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

def test_to_dict_no_missing_data():
    # Arrange
    test_data = Book(id = 1,
                    title="Harry Potter and the Chamber of Secrets",
                    description="Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past.")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] == "Harry Potter and the Chamber of Secrets"
    assert result["description"] == "Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past."

def test_to_dict_missing_id():
    # Arrange
    test_data = Book(title="Harry Potter and the Chamber of Secrets",
                    description="Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past.")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] is None
    assert result["title"] == "Harry Potter and the Chamber of Secrets"
    assert result["description"] == "Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past."

def test_to_dict_missing_title():
    # Arrange
    test_data = Book(id=1,
                    description="Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past.")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] is None
    assert result["description"] == "Harry returns to Hogwarts where a mysterious chamber is opened, unleashing a deadly secret from the school\'s past."

def test_to_dict_missing_description():
    # Arrange
    test_data = Book(id = 1,
                    title="Harry Potter and the Chamber of Secrets")

    # Act
    result = test_data.to_dict()

    # Assert
    assert len(result) == 3
    assert result["id"] == 1
    assert result["title"] == "Harry Potter and the Chamber of Secrets"
    assert result["description"] is None