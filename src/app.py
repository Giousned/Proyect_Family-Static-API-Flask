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

@app.route('/members', methods=['GET'])
def get_all_members():

    # this is how you can use the Family datastructure by calling its methods
    response = jackson_family.get_all_members()

    if response["code"] == 500:
        return jsonify({"error": "Ha habido un error en el servidor"}), 500
    if response["code"] == 200:
        return jsonify(response["members"]), 200

@app.route('/member', methods=['POST'])
def post_member():

    new_member = request.json

    response = jackson_family.add_member(new_member)

    if response["code"] == 500:
        return jsonify({"mensaje": "Ha habido un error en el servidor"}), 500
    if response["code"] == 200:
        return jsonify(response["members"]), 200

@app.route('/member/<int:id>', methods=['GET', 'DELETE'])
def get_member(id):

    if request.method == 'GET':
        response = jackson_family.get_member(id)

        if response["code"] == 500:
            return jsonify({"mensaje": "Ha habido un error en el servidor"}), 500
        if response["code"] == 200:
            return jsonify(response["member"]), 200
    
    if request.method == 'DELETE':
        response = jackson_family.delete_member(id)

        if response["code"] == 500:
            return jsonify({"mensaje": "Ha habido un error en el servidor"}), 500
        if response["code"] == 200:
            return jsonify({"done": True}), 200


# OTRA FORMA DE HACER, SIN PONER VARIOS METODOS JUNTOS
# @app.route('/member/<int:id>', methods=['DELETE'])
# def delete_member(id):

#     member = jackson_family.delete_member(id)

#     all_members = jackson_family.get_all_members()

#     return jsonify({"done": True}), 200

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
