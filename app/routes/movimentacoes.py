
from flask import Blueprint, render_template, redirect, url_for, flash

from app.forms.movimentacao_form import (
    MovimentacaoForm,
    carregar_produtos
)

from app.services.estoque_service import (
    registrar_movimentacao,
    listar_movimentacoes
)

movimentacoes = Blueprint("movimentacoes", __name__)


@movimentacoes.route("/movimentacoes/nova", methods=["GET", "POST"])
def nova_movimentacao():

    form = MovimentacaoForm()

    carregar_produtos(form)

    if form.validate_on_submit():

        try:
            registrar_movimentacao(
                produto_id=form.produto_id.data,
                tipo=form.tipo.data,
                quantidade=form.quantidade.data,
                motivo=form.motivo.data
            )

            flash(
                "Movimentação registrada com sucesso!",
                "success"
            )

            return redirect(url_for("movimentacoes.nova_movimentacao"))

        except ValueError as erro:
            flash(str(erro), "danger")

        except Exception:
            flash(
                "Ocorreu um erro ao registrar a movimentação.",
                "danger"
            )

    return render_template(
        "movimentacoes/nova.html",
        form=form
    )


@movimentacoes.route("/movimentacoes")
def listar():

    historico = listar_movimentacoes()

    return render_template(
        "movimentacoes/listar.html",
        movimentacoes=historico
    )
