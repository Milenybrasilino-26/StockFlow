from app import db

class Categoria(db.Model): #transforma a classe em um modelo de tabela.

    __tablename__ = "categorias" #define o nome da tabela no SQLite.

    id = db.Column(
        db.Integer, 
        primary_key=True
    ) #define a chave primária.

    nome = db.Column(
        db.String(100),
        unique=True, #impede nomes duplicados.
        nullable=False #impede nomes duplicados.
    )

    descricao = db.Column(
        db.String(255),
        nullable=True
    )

    produtos = db.relationship( #estabelece o relacionamento entre modelos.
        "Produto",
        back_populates="categoria"
    )

    def __repr__(self):
        return f"<Categoria {self.nome}>"