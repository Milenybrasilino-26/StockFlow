from app import db
from flask_login import UserMixin # fornece funcionalidades que o Flask-Login utiliza para identificar e gerenciar usuários autenticados.

class Usuario(UserMixin, db.Model):

    __tablename__ = "usuarios"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    email = db.Column(
        db.String(120),
        unique=True,
        nullable=False
    )

    senha_hash = db.Column(
        db.String(255),
        nullable=False
    )

    criado_em = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now()
    )

    movimentacoes = db.relationship(
        "Movimentacao",
        back_populates="usuario"
    )

    def __repr__(self):
        return f"<Usuario {self.nome}>"