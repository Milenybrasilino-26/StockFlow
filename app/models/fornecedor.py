from app import db

class Fornecedor(db.Model):
    __tablename__ = "Fornecedores"

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
        nullable=True
    )

    telefone = db.Column(
        db.String(20),
        nullable=True
    )

    produtos = db.relationship(
        "Produto",
        back_populates="fornecedor"
    )

    def __repr__(self):
        return f"<Fornecedor {self.nome}>"