from app import create_app, db
from app.models import Categoria, Fornecedor, Produto

app = create_app()

with app.app_context():

    try:
        # Criando uma categoria
        categoria = Categoria(
            nome="Periféricos",
            descricao="Acessórios e equipamentos"
        )

        # Criando um fornecedor
        fornecedor = Fornecedor(
            nome="Tech Distribuidora",
            email="contato@tech.com",
            telefone="11999999999"
        )

        db.session.add(categoria)
        db.session.add(fornecedor)

        # Salvando categoria e fornecedor
        db.session.flush()

        # Criando um produto relacionado aos dois
        produto = Produto(
            sku="MOUSE-001",
            nome="Mouse Gamer",
            categoria_id=categoria.id,
            fornecedor_id=fornecedor.id,
            quantidade=0,
            estoque_minimo=5,
            preco_custo_centavos=5000,
            preco_venda_centavos=8990
        )

        db.session.add(produto)

        # Confirmando as operações
        db.session.commit()

        print("Cadastro realizado com sucesso!")

        print(f"Produto: {produto.nome}")
        print(f"Categoria: {produto.categoria.nome}")
        print(f"Fornecedor: {produto.fornecedor.nome}")

    except Exception as erro:
        db.session.rollback()
        print(f"Erro ao cadastrar: {erro}")