"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET', 'POST'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    if  request.method == 'GET':
        members = jackson_family.get_all_members()
        response_body = {
        "hello": "world",
        "family": members
         }

        return jsonify(response_body), 200
    if request.method == 'POST':
        response_body = {}
        data = request.json
        results = jackson_family.add_member(data)
        response_body['message'] = 'Mienbro agregado'
        response_body['results'] = results
        return response_body, 200


@app.route('/members/<int:id>', methods=['GET', 'DELETE'])
def hadle_member(id):
    if request.method == 'GET':
        results = jackson_family.get_member(id)
        if results == []:
            response_body = {'message': 'No encontrado'}
            return response_body, 405
        response_body = {'member': results}
        return response_body, 200
    if request.method == 'DELETE':
        results = jackson_family.delete_member(id)
        response_body = {'message': 'Eliminado',
                         'results': results}
        return 


# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
