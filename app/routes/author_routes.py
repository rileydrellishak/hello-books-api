from flask import Blueprint, abort, make_response, request, Response
from app.models.author import Author
from app.models.book import Book
from ..db import db
from .route_utilities import validate_model, create_model

bp = Blueprint('author_bp', __name__, url_prefix='/authors')

@bp.post("")
def create_author():
    request_body = request.get_json()
    return create_model(Author, request_body)

@bp.get('/<author_id>')
def get_author_by_id(author_id):
    author = validate_model(Author, author_id)
    return author.to_dict()

@bp.get("")
def get_all_authors():
    query = db.select(Author)

    name_param = request.args.get("name")
    if name_param:
        query = query.where(Author.name.ilike(f"%{name_param}%"))

    authors = db.session.scalars(query.order_by(Author.id))
    # Use list comprehension syntax to create the list `authors_response`
    authors_response = [author.to_dict() for author in authors]

    return authors_response

@bp.get('/<author_id>/books')
def get_books_by_author(author_id):
    author = validate_model(Author, author_id)
    response = [book.to_dict() for book in author.books]
    return response

@bp.post('/<author_id>/books')
def create_book_with_author(author_id):
    author = validate_model(Author, author_id)
    request_body = request.get_json()
    request_body['author_id'] = author.id
    
    return create_model(Book, request_body)

@bp.put('/<author_id>')
def update_author(author_id):
    author = validate_model(Author, author_id)
    request_body = request.get_json()

    author.title = request_body['name']
    db.session.commit()

    return Response(status=204, mimetype='applications/json')

@bp.delete('/<author_id>')
def delete_book(author_id):
    author = validate_model(Author, author_id)

    db.session.delete(author)
    db.session.commit()

    return Response(status=204, mimetype='application/json')