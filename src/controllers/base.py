import json
from flask import Response, request
from flask_restful import Resource
from flask import jsonify

class BaseController(Resource):


    def __init__(self):
        pass

    def return_error(self, message: str, status: int) -> Response:
        response_json = json.dumps({'error-message': message})

        return Response(response_json, status, mimetype='application/json')

    def return_response(self, response_object, status: int = 200) -> Response:
        response_json = json.dumps({'data': response_object})

        return Response(response_json, status, mimetype='application/json')

    #pattern interessante
    def get_json_from_request(self):
        return request.get_json()

    def to_json(self, data):
        return jsonify(data)
