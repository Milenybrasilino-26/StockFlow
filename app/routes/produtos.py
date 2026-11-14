from flask import Blueprint, render_template, redirect, url_for, flash, request
from sqlalchemy import or_

from app import db
from app.models import Produto
from app.forms.produto_form import ProdutoForm, carregar_opcoes

produtos = Blueprint("produtos", __name__)


@produtos.route("/produtos/novo", methods=["GET", "POST"])
def novo_produto():

    form = ProdutoForm()

    # Carrega as categorias e os fornecedores
    carregar_opcoes(form)

    if form.validate_on_submit():

        fornecedor_id = form.fornecedor_id.data

        if fornecedor_id == 0:
            fornecedor_id = None

        produto = Produto(
            sku=form.sku.data.strip(),
            nome=form.nome.data.strip(),
            categoria_id=form.categoria_id.data,
            fornecedor_id=fornecedor_id,
            quantidade=0,
            estoque_minimo=form.estoque_minimo.data,
            preco_custo_centavos=int(form.preco_custo.data * 100),
            preco_venda_centavos=int(form.preco_venda.data * 100)
        )

        try:
            db.session.add(produto)
            db.session.commit()

            flash("Produto cadastrado com sucesso!", "success")

            return redirect(url_for("produtos.novo_produto"))

        except Exception:
            db.session.rollback()

            flash(
                "Não foi possível cadastrar o produto. "
                "Verifique se o SKU já está cadastrado.",
                "danger"
            )

    return render_template(
        "produtos/novo.html",
        form=form
    )

@produtos.route("/produtos")
def listar_produtos():

    busca = request.args.get("busca", "").strip()

    consulta = Produto.query.filter_by(ativo=True)

    if busca:
        consulta = consulta.filter(
            or_(
                Produto.nome.ilike(f"%{busca}%"),
                Produto.sku.ilike(f"%{busca}%")
            )
        )

    lista_produtos = consulta.order_by(
        Produto.nome.asc()
    ).all()

    return render_template(
        "produtos/listar.html",
        produtos=lista_produtos,
        busca=busca
    )