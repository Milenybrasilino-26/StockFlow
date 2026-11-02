from app import db

class Produto(db.Model):
    __tablename__ = "Produtos"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    sku = db.Column(
        db.String(50),
        unique=True,
        nullable=False
    )

    nome = db.Column(
        db.String(150),
        nullable=False
    )

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey('categorias.id'),
        nullable=False
    )


    fornecedor_id = db.Column(
        db.Integer,
        db.ForeignKey("Fornecedores.id"),
        nullable=True
    )

    quantidade = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    estoque_minimo = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    preco_custo_centavos = db.Column(
        db.Integer,
        nullable=False
    )

    preco_venda_centavos = db.Column(
        db.Integer,
        nullable=False
    )

    ativo = db.Column(
        db.Boolean,
        nullable=False,
        default=True
    )

    categoria = db.relationship(
        "Categoria",
        back_populates="produtos"
    )

    fornecedor = db.relationship(
        "Fornecedor",
        back_populates="produtos"
    )

    movimentacoes = db.relationship(
        "Movimentacao",
        back_populates="produto"
    )

    def __repr__(self):
        return f"<Produto {self.nome}>"