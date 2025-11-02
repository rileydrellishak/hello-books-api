import pytest
from app.models.author import Author

def test_from_dict_returns_author(client):
    author_data = {'name': 'J.K. Rowling'}

    new_author = Author.from_dict(author_data)

    assert new_author.name == author_data['name']

def test_from_dict_with_no_name():
    author_data = {'title': 'words'}

    with pytest.raises(KeyError, match='name'):
        new_author = Author.from_dict(author_data)

def test_from_dict_with_extra_keys():
    author_data = {'name': 'J.K. Rowling', 'birthday': 'November 1'}

    new_author = Author.from_dict(author_data)
    assert new_author.name == author_data['name']
    assert not hasattr(Author, 'birthday')

def test_to_dict_no_missing_data():
    test_data = Author(id=1, name='J.K. Rowling')
    result = test_data.to_dict()
    assert len(result) == 2
    assert result['id'] == 1
    assert result['name'] == 'J.K. Rowling'

def test_to_dict_missing_id():
    test_data = Author(name='J.K. Rowling')
    result = test_data.to_dict()
    assert len(result) == 2
    assert result['id'] == None
    assert result['name'] == 'J.K. Rowling'

def test_to_dict_missing_name():
    test_data = Author(id=1)
    result = test_data.to_dict()
    assert len(result) == 2
    assert result['id'] == 1
    assert result['name'] == None