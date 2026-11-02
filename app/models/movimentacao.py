from app import db

class Movimentacao(db.Model):

    __tablename__ = "movimentacoes"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    produto_id = db.Column(
        db.Integer,
        db.ForeignKey("Produtos.id"),
        nullable=False
    )

    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey("usuarios.id"),
        nullable=True
    )

    tipo = db.Column(
        db.String(20),
        nullable=False
    )

    quantidade = db.Column(
        db.Integer,
        nullable=False
    )

    motivo = db.Column(
        db.String(255),
        nullable=False
    )

    data_movimentacao = db.Column(
        db.DateTime,
        nullable=False,
        server_default=db.func.now()
    )

    produto = db.relationship(
        "Produto",
        back_populates="movimentacoes"
    )

    usuario = db.relationship(
        "Usuario",
        back_populates="movimentacoes"
    )

    def __repr__(self):
        return f"<Movimentacao {self.tipo}: {self.quantidade}>"