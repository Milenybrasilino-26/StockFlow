from app import create_app, db
from app.models import Produto, Movimentacao
from app.services.estoque_service import registrar_movimentacao

app = create_app()

with app.app_context():

    produto = Produto.query.filter_by(
        sku="MOUSE-001"
    ).first()

    if produto is None:
        raise ValueError("Produto não encontrado.")

    estoque_inicial = produto.quantidade

    movimentacoes_iniciais = Movimentacao.query.filter_by(
        produto_id=produto.id
    ).count()

    print(f"Estoque atual: {estoque_inicial}")

    try:
        registrar_movimentacao(
            produto_id=produto.id,
            tipo="SAIDA",
            quantidade=10,
            motivo="Teste de estoque insuficiente"
        )

        print("Atenção: a saída foi realizada!")

    except ValueError as erro:
        print(f"\nOperação bloqueada: {erro}")

    # Conferindo se o estoque permaneceu igual
    db.session.refresh(produto)

    movimentacoes_finais = Movimentacao.query.filter_by(
        produto_id=produto.id
    ).count()

    print(f"\nEstoque após o teste: {produto.quantidade}")

    print(
        f"Histórico antes: {movimentacoes_iniciais}"
    )

    print(
        f"Histórico depois: {movimentacoes_finais}"
    )

    if (
        produto.quantidade == estoque_inicial
        and movimentacoes_finais == movimentacoes_iniciais
    ):
        print("\nTESTE APROVADO!")
    else:
        print("\nTESTE FALHOU!")