
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, StringField, SubmitField
from wtforms.validators import DataRequired, NumberRange, Length

from app.models import Produto


class MovimentacaoForm(FlaskForm):

    produto_id = SelectField(
        "Produto",
        coerce=int,
        validators=[DataRequired()]
    )

    tipo = SelectField(
        "Tipo de movimentação",
        choices=[
            ("ENTRADA", "Entrada"),
            ("SAIDA", "Saída")
        ],
        validators=[DataRequired()]
    )

    quantidade = IntegerField(
        "Quantidade",
        validators=[
            DataRequired(),
            NumberRange(min=1, message="A quantidade deve ser maior que zero.")
        ]
    )

    motivo = StringField(
        "Motivo",
        validators=[
            DataRequired(message="Informe o motivo da movimentação."),
            Length(max=255)
        ]
    )

    submit = SubmitField("Registrar movimentação")


def carregar_produtos(form):

    produtos = Produto.query.filter_by(
        ativo=True
    ).order_by(
        Produto.nome.asc()
    ).all()

    form.produto_id.choices = [
        (produto.id, f"{produto.sku} - {produto.nome}")
        for produto in produtos
    ]
