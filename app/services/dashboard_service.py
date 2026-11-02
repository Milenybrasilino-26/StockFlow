from sqlalchemy import func

from app import db
from app.models import Produto


def obter_indicadores_estoque():

    # Quantidade de produtos ativos
    total_produtos = db.session.query(
        func.count(Produto.id)
    ).filter(
        Produto.ativo.is_(True)
    ).scalar() or 0

    # Quantidade total de unidades disponíveis
    total_unidades = db.session.query(
        func.sum(Produto.quantidade)
    ).filter(
        Produto.ativo.is_(True)
    ).scalar() or 0

    # Produtos que atingiram o estoque mínimo
    produtos_estoque_baixo = db.session.query(
        func.count(Produto.id)
    ).filter(
        Produto.ativo.is_(True),
        Produto.quantidade <= Produto.estoque_minimo
    ).scalar() or 0

    # Valor estimado do estoque pelo preço de custo
    valor_estoque = db.session.query(
        func.sum(
            Produto.quantidade * Produto.preco_custo_centavos
        )
    ).filter(
        Produto.ativo.is_(True)
    ).scalar() or 0

    return {
        "total_produtos": total_produtos,
        "total_unidades": total_unidades,
        "produtos_estoque_baixo": produtos_estoque_baixo,
        "valor_estoque_centavos": valor_estoque
    }