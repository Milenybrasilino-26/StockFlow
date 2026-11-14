
from sqlalchemy import func

from app import db
from app.models import Produto, Movimentacao


def obter_indicadores_estoque():

    # Quantidade de produtos ativos
    total_produtos = db.session.query(
        func.count(Produto.id)
    ).filter(
        Produto.ativo.is_(True)
    ).scalar() or 0

    # Quantidade total de unidades
    total_unidades = db.session.query(
        func.sum(Produto.quantidade)
    ).filter(
        Produto.ativo.is_(True)
    ).scalar() or 0

    # Produtos com estoque baixo
    produtos_estoque_baixo = db.session.query(
        func.count(Produto.id)
    ).filter(
        Produto.ativo.is_(True),
        Produto.quantidade <= Produto.estoque_minimo
    ).scalar() or 0

    # Valor estimado do estoque
    valor_estoque = db.session.query(
        func.sum(
            Produto.quantidade * Produto.preco_custo_centavos
        )
    ).filter(
        Produto.ativo.is_(True)
    ).scalar() or 0

    # Total de movimentações registradas
    total_movimentacoes = db.session.query(
        func.count(Movimentacao.id)
    ).scalar() or 0

    # Cinco movimentações mais recentes
    movimentacoes_recentes = Movimentacao.query.order_by(
        Movimentacao.data_movimentacao.desc()
    ).limit(5).all()

    # Produtos que precisam de reposição
    lista_produtos_estoque_baixo = Produto.query.filter(
        Produto.ativo.is_(True),
        Produto.quantidade <= Produto.estoque_minimo
    ).order_by(
        Produto.quantidade.asc()
    ).limit(5).all()

    return {
        "total_produtos": total_produtos,
        "total_unidades": total_unidades,
        "produtos_estoque_baixo": produtos_estoque_baixo,
        "valor_estoque_centavos": valor_estoque,
        "total_movimentacoes": total_movimentacoes,
        "movimentacoes_recentes": movimentacoes_recentes,
        "lista_produtos_estoque_baixo": lista_produtos_estoque_baixo
    }
