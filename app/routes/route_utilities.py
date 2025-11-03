from flask import abort, make_response, request
from ..db import db

def validate_model(cls, model_id):
    try:
        model_id = int(model_id)
    except:
        response = {"message": f"{cls.__name__} {model_id} invalid"}
        abort(make_response(response , 400))

    query = db.select(cls).where(cls.id == model_id)
    model = db.session.scalar(query)
    
    if not model:
        response = {"message": f"{cls.__name__} {model_id} not found"}
        abort(make_response(response, 404))
    
    return model

def create_model(cls, model_data):

    try:
        new_instance = cls.from_dict(model_data)
    
    except KeyError as error:
        response = {'message': f'Invalid request: missing {error.args[0]}'}
        abort(make_response(response, 400))
    
    db.session.add(new_instance)
    db.session.commit()

    return make_response(new_instance.to_dict(), 201)

# Move code that queries, filters, and returns a JSON representation of model records to a new function named get_models_with_filters in route_utilities.py

def get_models_with_filters(cls, filters=None):
    query = db.select(cls)

    if filters:
        for attribute, value in filters.items():
            if hasattr(cls, attribute):
                query = query.where(getattr(cls, attribute).ilike(f"%{value}%"))

    query = query.order_by(cls.id)
    models = db.session.scalars(query)

    response = [model.to_dict() for model in models]
    return response