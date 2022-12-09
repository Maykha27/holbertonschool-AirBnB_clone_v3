#!/usr/bin/python3
"""
    countains the states view
"""

from api.v1.views import app_views
from models import storage
from models.state import State
from flask import request
import json

@app_views.route('/states/', methods = ['POST'])
def post_States():
    """Retrieve a list of all State objects or retrieve html request"""
    dict = request.get_json()
    if dict is None:
        return ("Not a JSON"), 400
    if dict['name'] is None:
        return ("Missing name"), 400
    new_state = State(**dict)
    storage.save()
    return (new_state.to_dict()), 201

@app_views.route('/states/')
def get_States():
    return (1)
    states_list = []
    for state in storage.all('State').values():
        states_list.append(state.to_dict())
    return (states_list)

for state in storage.all('State').values():
    @app_views.route('/states/' + state.id, methods = ['PUT', 'DELETE','GET'])
    def get_State():
        """Get, Delete, Put, and Post a State objects"""

        if request.method == 'DELETE':
            """delete method: get obj frome db, then delete it, save"""
            delstate = storage.get(state.__class__, state.id)
            if delstate is None:
                return '"error": "Not found"', 404
            delstate.delete()
            storage.save()
            return ({}), 200

        if request.method == 'PUT':
            """ Put method: get obj frome db, then change attributes
                (not time or id), save"""
            dict = request.get_json()
            putstate = storage.get(state.__class__, state.id)
            if putstate is None:
                return '"error": "Not found"', 404
            if dict is None:
                return ("Not a JSON"), 400
            for key, value in dict.items():
                if key not in ('id', 'created_at', 'updated_at'):
                    setattr(putstate, key, value)
            storage.save()
            return (putstate.to_dict()), 200

        else:
            """Get method: get obj frome db, then return it"""

            getstate = storage.get(state.__class__, state.id)
            if getstate is None:
                return '"error": "Not found"', 404
            return getstate.to_dict()

    get_State.__name__ = state.id
