from app import create_app, db
from app.models import Produto, Movimentacao
from app.services.estoque_service import registrar_movimentacao

app = create_app()

with app.app_context():

    try:
        # Buscar o produto cadastrado anteriormente
        produto = Produto.query.filter_by(
            sku="MOUSE-001"
        ).first()

        if produto is None:
            raise ValueError("Produto não encontrado.")

        print(f"Produto: {produto.nome}")
        print(f"Estoque inicial: {produto.quantidade}")

        # Registrar entrada de 5 unidades
        registrar_movimentacao(
            produto_id=produto.id,
            tipo="ENTRADA",
            quantidade=5,
            motivo="Reposição de estoque"
        )

        print("\nEntrada registrada!")

        # Registrar saída de 2 unidades
        registrar_movimentacao(
            produto_id=produto.id,
            tipo="SAIDA",
            quantidade=2,
            motivo="Venda de produto"
        )

        print("Saída registrada!")

        # Consultar novamente o produto
        db.session.refresh(produto)

        print(f"\nEstoque final: {produto.quantidade}")

        # Consultar histórico
        movimentacoes = Movimentacao.query.filter_by(
            produto_id=produto.id
        ).order_by(
            Movimentacao.id.desc()
        ).limit(2).all()

        print("\nHISTÓRICO DE MOVIMENTAÇÕES")

        for movimentacao in movimentacoes:
            print(
                f"{movimentacao.tipo} - "
                f"{movimentacao.quantidade} unidades - "
                f"{movimentacao.motivo}"
            )

    except Exception as erro:
        print(f"\nErro no teste: {erro}")