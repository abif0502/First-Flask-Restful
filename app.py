# Import library

from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

# initialize object

app = Flask(__name__)

# Initialize flask restful
api = Api(app)

# Initialize flask cors
CORS(app)

identitas = {}

# Kelas resource


class ContohResource(Resource):
    # GET
    def get(self):
        # response = {"msg": "Hello World"}

        return identitas
    # Post

    def post(self):
        nama = request.form["nama"]
        usia = int(request.form["usia"])

        identitas["nama"] = nama
        identitas["usia"] = usia

        return {"msg": "data berhasil ditambahkan"}


# Setup resource
api.add_resource(ContohResource, "/api", methods=["GET", "POST"])

if __name__ == "__main__":
    app.run(debug=True, port=5005)
