from api.v1.views import app_views
import json


@app_views.route('/status')
def status():
    json_dict = {
        "status": "OK"
        }
    return json.dumps(json_dict)
