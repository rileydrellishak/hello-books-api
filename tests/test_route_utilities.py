from werkzeug.exceptions import HTTPException
import pytest
from app.models.book import Book
from app.models.author import Author
from app.routes.route_utilities import validate_model, create_model, get_models_with_filters

def test_validate_model(two_saved_books):
    # Act
    result_book = validate_model(Book, 1)

    # Assert
    assert result_book.id == 1
    assert result_book.title == "Twilight"
    assert result_book.description == "A supernatural romance about a teenage girl who falls in love with a mysterious vampire, blurring the line between danger and desire."

def test_validate_model_missing_record(two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException) as error:
        result_book = validate_model(Book, 3)
    
    response = error.value.response
    assert response.status == "404 NOT FOUND"
    
def test_validate_model_invalid_id(two_saved_books):
    # Act & Assert
    # Calling `validate_model` without being invoked by a route will
    # cause an `HTTPException` when an `abort` statement is reached 
    with pytest.raises(HTTPException) as error:
        result_book = validate_model(Book, "cat")
    
    response = error.value.response
    assert response.status == "400 BAD REQUEST"

def test_create_model_book(client):
    test_data = {
        'title': 'Twilight',
        'description': 'A captivating love story between a human girl and a vampire whose worlds are never meant to collide.'
    }
    result = create_model(Book, test_data)

    assert result.status_code == 201
    assert result.get_json() == {
        'id': 1,
        'title': 'Twilight',
        'description': 'A captivating love story between a human girl and a vampire whose worlds are never meant to collide.'
    }

def test_create_model_book_extra_keys(client):
    test_data = {
        'title': 'Twilight',
        'description': 'A captivating love story between a human girl and a vampire whose worlds are never meant to collide.',
        'where to buy': 'Barnes & Noble'
    }
    result = create_model(Book, test_data)

    assert result.status_code == 201
    assert result.get_json() == {
        'id': 1,
        'title': 'Twilight',
        'description': 'A captivating love story between a human girl and a vampire whose worlds are never meant to collide.'
    }

def test_create_model_book_missing_keys(client):
    test_data = {
        'title': 'Twilight'
        }
    
    with pytest.raises(HTTPException) as error:
        result_book = create_model(Book, test_data)

    response = error.value.response
    assert response.status == "400 BAD REQUEST"

def test_create_model_author(client):
    test_data = {
        'name': 'stephenie Meyer'
    }

    result = create_model(Author, test_data)
    
    assert result.status_code == 201
    assert result.get_json() == {
        'id': 1,
        'name': 'stephenie Meyer'
    }

def test_create_model_author_extra_keys(client):
    test_data = {
        'name': 'stephenie Meyer'
    }

    result = create_model(Author, test_data)

def test_create_model_author_missing_data(client):
    test_data = {
        'name': 'stephenie Meyer'
    }

    with pytest.raises(HTTPException) as error:
        result_book = create_model(Book, test_data)

    response = error.value.response
    assert response.status == "400 BAD REQUEST"

def test_get_models_with_filters_book(client, two_saved_books):
    result = get_models_with_filters(Book, {'title': 'Twilight'})
    assert result == [{
        'id': 1,
        'title': 'Twilight',
        'description': 'A supernatural romance about a teenage girl who falls in love with a mysterious vampire, blurring the line between danger and desire.'
        }]
    
def test_get_models_with_filters_author(client, two_saved_authors):
    result = get_models_with_filters(Author, {'name': 'R.F. Kuang'})
    assert result == [{
        'id': 1,
        'name': 'R.F. Kuang'
    }]

def test_get_models_with_filters_author_no_dict(client, two_saved_authors):
    result = get_models_with_filters(Author)
    assert result == [
        {'id': 1, 'name': 'R.F. Kuang'},
        {'id': 2, 'name': 'Stephenie Meyer'}
        ]