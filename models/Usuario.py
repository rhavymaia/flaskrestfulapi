from helpers.database import db
# Mapeamento do marshal
# Mapeamento ORM
# Construtor do objeto.


class Usuario(db.Model):

    __tablename__ = "tb_usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(150), nullable=False)
    cpf = db.Column(db.String(11), nullable=False)

    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

    def __repr__(self):
        pass
