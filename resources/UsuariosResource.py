from flask_restful import Resource, reqparse

usuarios = [{'nome': 'João'}, {'nome': 'Maria'}]


class UsuariosResource(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument(
            'nome', type=str, help='Nome obrigatório', required=True)
        self.parser.add_argument(
            'nascimento', type=str, help='Nascimento obrigatório', required=True)

    def get(self):
        return (usuarios, 200)

    def post(self):
        args = self.parser.parse_args()
        return {'id': 1, 'nome': args['nome'], 'nascimento': args['nascimento']}


class UsuarioResource(Resource):
    def get(self, usuario_id=None):
        return {'id': usuario_id}

    def put(self, usuario_id):
        return {}

    def delete(self, usuario_id):
        return {}
