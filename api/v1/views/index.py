#!/usr/bin/python3
"""
    countains the blueprint for our "app" flask server
"""

from api.v1.views import app_views
from models import storage

classes = ("Amenity", "City", "Place", "Review", "State", "User")

@app_views.route('/status')
def status():
    """returns the current status"""
    dict = {
        "status": "OK"
        }
    return dict

@app_views.route('/stats')
def stats():
    """Returns the number of instances in each class"""
    count_dict = {}
    for clas in classes:
        count_dict[clas] = storage.count(clas)

    return(count_dict)

