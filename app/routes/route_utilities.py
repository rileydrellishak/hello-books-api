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

# Move code that creates and returns a JSON representation of a model to a new function named create_model in route_utilities.py

# Move all the common code from create author, create book with author, create book
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