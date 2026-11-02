from app import create_app
from app.models import Produto
from app.services.estoque_service import listar_movimentacoes

app = create_app()

with app.app_context():

    produto = Produto.query.filter_by(
        sku="MOUSE-001"
    ).first()

    if produto is None:
        raise ValueError("Produto não encontrado.")

    # Consultar todas as movimentações do produto
    historico = listar_movimentacoes(
        produto_id=produto.id
    )

    print("\nHISTÓRICO DO PRODUTO")
    print(f"Produto: {produto.nome}")
    print("-" * 45)

    for movimentacao in historico:

        print(f"Tipo: {movimentacao.tipo}")
        print(f"Quantidade: {movimentacao.quantidade}")
        print(f"Motivo: {movimentacao.motivo}")
        print(f"Data: {movimentacao.data_movimentacao}")
        print("-" * 45)