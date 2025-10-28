def test_get_all_books_with_no_records(client):
    # Act
    response = client.get("/books")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == []

def test_get_one_book(client, two_saved_books):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "title": "Twilight",
        "description": "A supernatural romance about a teenage girl who falls in love with a mysterious vampire, blurring the line between danger and desire."
    }

def test_create_one_book(client):
    # Act
    response = client.post("/books", json={
        "title": "Eclipse",
        "description": "Bella is forced to choose between her love for Edward and her friendship with Jacob amid rising supernatural tensions."
    })
    response_body = response.get_json()

    # Assert
    assert response.status_code == 201
    assert response_body == {
        "id": 1,
        "title": "Eclipse",
        "description": "Bella is forced to choose between her love for Edward and her friendship with Jacob amid rising supernatural tensions."
    }

def test_get_one_book_from_empty_db_404(client):
    # Act
    response = client.get("/books/1")
    response_body = response.get_json()

    # Assert
    assert response.status_code == 404
    assert response_body == {'message': f'book 1 not found'}