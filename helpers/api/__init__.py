from flask_restful import Api
from flask import Blueprint

from resources.IndexResource import IndexResource
from resources.UsuariosResource import UsuariosResource, UsuarioResource

blueprint = Blueprint('api', __name__)

api = Api(blueprint, prefix="/api")

api.add_resource(IndexResource, '/')
api.add_resource(UsuariosResource, '/usuarios')
api.add_resource(UsuarioResource, '/usuarios/<string:usuario_id>')
