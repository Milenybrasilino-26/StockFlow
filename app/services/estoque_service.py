from app import db
from app.models import Produto, Movimentacao


def registrar_movimentacao(
    produto_id,
    tipo,
    quantidade,
    motivo,
    usuario_id=None
):
    tipo = tipo.strip().upper()

    # Validar o tipo de movimentação
    if tipo not in ["ENTRADA", "SAIDA"]:
        raise ValueError("Tipo de movimentação inválido.")

    # Validar a quantidade
    if not isinstance(quantidade, int) or isinstance(quantidade, bool) or quantidade <= 0:
        raise ValueError("A quantidade deve ser um número inteiro positivo.")

    if not motivo or not motivo.strip():
        raise ValueError("O motivo da movimentação é obrigatório.")

    # Buscar o produto
    produto = db.session.get(Produto, produto_id)

    if produto is None:
        raise ValueError("Produto não encontrado.")

    if not produto.ativo:
        raise ValueError("Não é possível movimentar um produto inativo.")

    # Verificar estoque disponível
    if tipo == "SAIDA" and produto.quantidade < quantidade:
        raise ValueError("Estoque insuficiente para realizar a saída.")

    try:
        # Atualizar a quantidade
        if tipo == "ENTRADA":
            produto.quantidade += quantidade
        else:
            produto.quantidade -= quantidade

        # Registrar a movimentação
        movimentacao = Movimentacao(
            produto_id=produto.id,
            usuario_id=usuario_id,
            tipo=tipo,
            quantidade=quantidade,
            motivo=motivo
        )

        db.session.add(movimentacao)

        # Salvar as duas alterações juntas
        db.session.commit()

        return movimentacao

    except Exception:
        db.session.rollback()
        raise

def listar_produtos_estoque_baixo():
    produtos = Produto.query.filter(
        Produto.ativo.is_(True),
        Produto.quantidade <= Produto.estoque_minimo
    ).order_by(
        Produto.quantidade.asc()
    ).all()

    return produtos


def listar_movimentacoes(
        produto_id=None,
        tipo=None,
        limite=50
):
    consulta = Movimentacao.query

    if produto_id is not None:
        consulta = consulta.filter(
             Movimentacao.produto_id == produto_id
        )

    if tipo:
        tipo = tipo.strip().upper()

        if tipo not in ['ENTRADA', 'SAIDA']:
            raise ValueError("Tipo de movimentação Inválida!")

        consulta = consulta.filter(
            Movimentacao.tipo == tipo
        )

    consulta = consulta.order_by(
        Movimentacao.data_movimentacao.desc(),
        Movimentacao.id.desc()
    )

    return consulta.limit(limite).all()