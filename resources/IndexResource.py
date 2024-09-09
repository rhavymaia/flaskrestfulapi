from flask_restful import Resource


class IndexResource(Resource):
    def get(self):
        return {'versao': '0.1'}

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass
